"""Build clean CSVs, SQLite databases, SQL results, validation and case studies.

Run from any directory: python -m portfolio.run --root /path/to/repository
All outputs are deterministic for the same source files and software versions.
"""
import argparse
import hashlib
import html
import json
import platform
import re
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import scipy

from .contracts import PROJECTS, STAGES, ONBOARDING
from .metrics import experiment, ratio
from .quality import clean_table, foreign_key, ordered_funnel


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True, allow_nan=False)+'\n')


def read_queries(path):
    sections = re.split(r'^-- name: (\w+)\s*$', path.read_text(), flags=re.M)
    if sections[0].strip() or len(sections)<3:
        raise ValueError(f'Invalid query file: {path}')
    return list(zip(sections[1::2], sections[2::2]))


def check_equal(name, actual, expected, checks):
    if actual is None or expected is None:
        match = actual is None and expected is None
    else:
        match = bool(np.allclose(actual,expected,rtol=1e-10,atol=1e-8))
    checks.append({'check':name,'passed':match})
    if not match:
        raise AssertionError(f'{name}: SQL={actual}, independent Python={expected}')


def validate_relations(key, t, checks):
    """Blocking relational checks plus nonblocking semantic diagnostics."""
    issues=[]
    def require(name, condition):
        passed=bool(condition);checks.append({'check':name,'passed':passed})
        if not passed: raise ValueError(name)
    def warn(name, count, explanation):
        issues.append({'issue':name,'affected_rows':int(count),'interpretation':explanation})
    if key.startswith('01'):
        u,s,e=t['users'],t['subscriptions'],t['events']
        foreign_key(s,u,'user_id');foreign_key(e,u,'user_id')
        require('subscription coverage',set(s.user_id)==set(u.user_id))
        joined=s.merge(u,on='user_id',suffixes=('_s','_u'))
        require('plan tiers agree',joined.plan_tier_s.eq(joined.plan_tier_u).all())
        require('valid plan tier',s.plan_tier.isin(['Free','Starter','Pro','Enterprise']).all())
        dated=e.merge(u[['user_id','signup_date']],on='user_id')
        warn('events_before_signup',(dated.event_date<dated.signup_date).sum(),'Retained in source; excluded by ordered funnels and 90-day activity windows.')
        flags=set(e.loc[e.event_name.eq('Step 2: Workspace'),'user_id'])
        warn('step2_flag_disagreement',s.completed_step2.ne(s.user_id.isin(flags).astype(int)).sum(),'Source flag and event presence are distinct signals; no silent overwrite.')
        warn('free_accounts_with_churn_label',((s.mrr==0)&(s.churned_within_90d==1)).sum(),'Exclude free accounts from paying-user churn rate. Label timing is not independently verified.')
    elif key.startswith('02'):
        require('exactly two experiment arms',set(t['ab_sessions'].variant)=={'Control','Variant B'})
        warn('unknown_randomization_unit',len(t['ab_sessions']),'No user ID or assignment metadata. Session independence and 50:50 allocation are assumptions; inference is provisional.')
    elif key.startswith('03'):
        w,o=t['web_sessions'],t['orders'];foreign_key(o,w,'session_id')
        require('purchase requires cart',(w.purchased<=w.added_to_cart).all())
        require('one order per purchased session',set(o.session_id)==set(w.loc[w.purchased==1,'session_id']))
        j=o.merge(w,on='session_id',suffixes=('_o','_w'))
        for col in ['session_date','device','channel']:
            require(f'order/session {col} agrees',j[col+'_o'].eq(j[col+'_w']).all())
    elif key.startswith('04'):
        s,l=t['sales'],t['listings'];foreign_key(s,l,'listing_id')
        j=s.merge(l,on='listing_id',suffixes=('_s','_l'))
        for col in ['seller_id','category','price','rating','in_stock']:
            require(f'sale/listing {col} agrees',j[col+'_s'].eq(j[col+'_l']).all())
        warn('revenue_not_price_times_units',((s.revenue-s.price*s.units_sold).abs()>0.011).sum(),'Use recorded revenue as supplied. Discounts, fees, tax and source-generation rules are unknown; do not call the difference an error or lost revenue.')
        warn('sales_on_out_of_stock_listings',s.in_stock.eq(0).sum(),'Stock flag is an undated snapshot; does not establish status at sale time or causal lost sales.')
    elif key.startswith('05'):
        u,e=t['users'],t['journey_events'];foreign_key(e,u,'user_id')
        require('known journey stages',set(e.journey_stage).issubset(set(STAGES+['Signup'])))
        expected={s:i for i,s in enumerate(STAGES+['Signup'],1)}
        require('stage order agrees',e.stage_order.eq(e.journey_stage.map(expected)).all())
        j=e.merge(u[['user_id','first_seen_date']],on='user_id')
        warn('events_before_first_seen',(j.event_date<j.first_seen_date).sum(),'Retained; ordered funnel and time-to-purchase exclude invalid temporal paths.')
        first=e.pivot_table(index='user_id',columns='journey_stage',values='event_date',aggfunc='min').apply(pd.to_datetime)
        inversions=pd.Series(False,index=first.index)
        for previous,following in zip(STAGES,STAGES[1:]):
            inversions |= first[previous].notna() & first[following].notna() & first[following].lt(first[previous])
        warn('users_with_adjacent_stage_date_inversions',inversions.sum(),'At least one later stage predates its preceding stage. Do not interpret strict ordered-path loss as business abandonment; investigate synthetic generation/tracking timestamps.')
    checks.append({'check':'foreign key checks completed','passed':True})
    return issues


def reconcile(key,t,out,checks):
    extra={}
    if key.startswith('01'):
        s=t['subscriptions'];row=out['summary'].iloc[0]
        for name,value in {'users':len(s),'paying_users':int((s.mrr>0).sum()),'snapshot_mrr':s.mrr.sum(),'snapshot_arr':s.mrr.sum()*12,'paying_churn_label_rate':s.loc[s.mrr>0,'churned_within_90d'].mean()}.items():
            check_equal(name,float(row[name]),float(value),checks)
        expected=ordered_funnel(t['users'],t['events'],ONBOARDING,'event_name','signup_date')
        check_equal('ordered onboarding SQL/Python',out['onboarding_funnel'].users.tolist(),expected,checks)
        e=t['events'].merge(t['users'][['user_id','signup_date']],on='user_id')
        event_date=pd.to_datetime(e.event_date);signup=pd.to_datetime(e.signup_date)
        mask=e.event_name.eq('Workflow Run') & e.event_group.eq('Product') & event_date.ge(signup) & event_date.lt(signup+pd.Timedelta(days=90))
        counts=e[mask].groupby('user_id').size()
        p=s[s.mrr>0].copy();p['activity_group']=np.where(p.user_id.map(counts).fillna(0)>=20,'20+ runs','Under 20 runs')
        for row in out['power_user_association'].itertuples():
            subgroup=p[p.activity_group==row.activity_group]
            check_equal('power user count '+row.activity_group,row.paying_users,len(subgroup),checks)
            check_equal('power user churn '+row.activity_group,row.churn_label_rate,subgroup.churned_within_90d.mean(),checks)
        extra['onboarding_step2_conditional_dropoff']=1-ratio(expected[1],expected[0]) if expected[0] else None
    elif key.startswith('02'):
        df=t['ab_sessions']
        for row in out['variant_summary'].itertuples():
            arm=df[df.variant.eq(row.variant)]
            for metric,value in {'sessions':len(arm),'conversions':arm.converted.sum(),'conversion_rate':arm.converted.mean(),'bounce_rate':arm.bounce.mean(),'mean_engagement':arm.engagement_score.mean(),'revenue':arm.revenue.sum(),'revenue_per_session':arm.revenue.mean()}.items():
                check_equal(row.variant+' '+metric,float(getattr(row,metric)),float(value),checks)
        a=df[df.variant.eq('Control')];b=df[df.variant.eq('Variant B')]
        extra['experiment']=experiment(int(a.converted.sum()),len(a),int(b.converted.sum()),len(b))
        extra['experiment']['decision']='Do not authorize rollout from simulated session-level evidence; verify randomization, user independence and business guardrails.'
    elif key.startswith('03'):
        w,o=t['web_sessions'],t['orders'];row=out['summary'].iloc[0]
        values={'sessions':len(w),'cart_sessions':w.added_to_cart.sum(),'purchases':w.purchased.sum(),'conversion_rate':w.purchased.mean(),'cart_abandonment_rate':1-w.purchased.sum()/w.added_to_cart.sum(),'revenue':o.order_value.sum(),'average_order_value':o.order_value.mean()}
        for name,value in values.items():check_equal(name,float(row[name]),float(value),checks)
        rev=o.groupby('sku').order_value.sum().sort_values(ascending=False)
        n=int(np.ceil(len(rev)*.2));share=float(rev.iloc[:n].sum()/rev.sum())
        sql=out['sku_pareto'];check_equal('top 20 percent SKU share',float(sql.loc[sql.in_top_20_percent==1,'revenue'].sum()/sql.revenue.sum()),share,checks)
        extra['top_20_percent_sku_revenue_share']=share
        extra['rfm_status']='Not computed: no stable customer ID; session_id is not a customer proxy.'
    elif key.startswith('04'):
        s=t['sales'];row=out['summary'].iloc[0]
        for name,value in {'sales_rows':len(s),'units':s.units_sold.sum(),'recorded_revenue':s.revenue.sum(),'price_times_units':(s.price*s.units_sold).sum(),'revenue_discrepancy_rows':((s.revenue-s.price*s.units_sold).abs()>.011).sum(),'sellers':s.seller_id.nunique()}.items():check_equal(name,float(row[name]),float(value),checks)
        seller=s.groupby('seller_id').revenue.sum().sort_values(ascending=False)
        share=float(seller.iloc[:10].sum()/seller.sum())
        check_equal('top ten seller share',float(out['seller_concentration'].head(10).revenue_share.sum()),share,checks)
        extra['top_10_seller_revenue_share']=share
        extra['seller_hhi']=float(((seller/seller.sum())**2).sum()*10000)
    else:
        u,e=t['users'],t['journey_events'];row=out['summary'].iloc[0]
        purchasers=set(e.loc[e.journey_stage.eq('Purchase'),'user_id'])
        check_equal('users',row.users,len(u),checks);check_equal('purchasers',row.purchasers,len(purchasers),checks)
        check_equal('observed purchase rate',row.observed_purchase_rate,len(purchasers)/len(u),checks)
        expected=ordered_funnel(u,e,STAGES,'journey_stage','first_seen_date')
        check_equal('ordered journey SQL/Python',out['ordered_funnel'].users.tolist(),expected,checks)
        j=e[e.journey_stage.eq('Purchase')].merge(u[['user_id','first_seen_date']],on='user_id')
        j=j[j.event_date>=j.first_seen_date].copy();j['days']=(pd.to_datetime(j.event_date)-pd.to_datetime(j.first_seen_date)).dt.days
        time=j.groupby('user_id').days.min()
        check_equal('time to purchase',out['time_to_purchase'].days_to_purchase.tolist(),time.sort_index().tolist(),checks)
        extra['p50_days_to_purchase']=float(time.quantile(.5)) if len(time) else None
        extra['p90_days_to_purchase']=float(time.quantile(.9)) if len(time) else None
        extra['ordered_path_loss_after_checkout']=1-ratio(expected[-1],expected[-2]) if expected[-2] else None
        extra['signup_handling']='Signup is reported separately; source ordinal 7 is not treated as a universal post-purchase requirement. Ordered-path loss is a tracking/sequence diagnostic, not validated checkout abandonment.'
    return extra


GUIDANCE={
 '01': ('SaaS activation and revenue quality',
 'Where does onboarding lose users, and how do observed activity and churn labels differ?',
 'Investigate the largest ordered onboarding drop-off with usability research. Treat activity/churn comparisons as associations; propose a randomized onboarding experiment before claiming retention impact.',
 'MRR/ARR are supplied snapshots, not recognized revenue or verified active run rates. Churn is a supplied 90-day label, not an independently reconstructed cohort outcome. Free users are excluded from paying churn. Repeated daily events are retained because event IDs are absent. Activity uses [signup, signup + 90 days); incomplete follow-up and reverse causality limit interpretation.'),
 '02': ('Experiment measurement and rollout judgment',
 'Does Variant B show higher session conversion, and how uncertain is the estimated difference?',
 'Use conversion as the primary metric; investigate bounce, revenue per session and engagement as guardrails. Verify assignment unit, exposure, intended allocation and experiment duration before a real rollout. Segment results are exploratory.',
 'Simulated session observations lack stable user IDs and assignment logs. The two-sided pooled z-test and Newcombe-Wilson interval assume independent trials. The sample-ratio test assumes 50:50 allocation. No claim of actual causal business impact is made; repeated peeking and multiple comparisons are not corrected.'),
 '03': ('Ecommerce funnel and merchandise concentration',
 'Which device/channel combinations lose cart sessions, and how concentrated is SKU revenue?',
 'Prioritize segments with both substantial session volume and high abandonment. Validate checkout friction with UX evidence; use SKU concentration to guide inventory review, not automatic assortment cuts.',
 'Each order row is one purchased session in this supplied dataset. This is a dataset contract, not a universal ecommerce model. No customer ID exists, so customer RFM and repeat-purchase claims are intentionally omitted. Discount comparisons are observational and may reflect product/segment selection.'),
 '04': ('Marketplace revenue and source reconciliation',
 'How concentrated is recorded seller revenue, and what prevents financial reconciliation?',
 'Resolve the difference between recorded revenue and price × units with a source owner before financial use. Review seller exposure by revenue share. Stock-status comparisons are diagnostic associations only.',
 'The supplied data do not identify orders, fees, Prime membership or seller tiers. Sales row count is not order count. Recorded revenue is not labeled platform revenue or GMV. Snapshot stock status is not historical inventory. Repeated fact rows are retained because there is no sale ID; no causal lost-revenue estimate is justified.'),
 '05': ('Ordered user journey and conversion friction',
 'How many users complete an ordered commerce path, and how does observed conversion differ by returning status?',
 'Compare overall purchase reach with the stricter ordered funnel and investigate missing or out-of-order tracking. Diagnose the largest eligible transition drop before proposing a UX test.',
 'Source dates have day granularity; same-day steps are allowed and cannot establish within-day order. Signup is separate from the six-step commerce funnel. First-seen cohorts have different follow-up durations, so conversion and time-to-purchase are descriptive, not censoring-adjusted causal measures.')}


def markdown_table(frame):
    def cell(v):
        if isinstance(v,(float,np.floating)): return f'{v:,.6g}'
        return str(v).replace('|','\\|')
    lines=['| '+' | '.join(frame.columns)+' |','| '+' | '.join(['---']*len(frame.columns))+' |']
    lines+=['| '+' | '.join(cell(v) for v in row)+' |' for row in frame.itertuples(index=False,name=None)]
    return '\n'.join(lines)


def chart(key, results):
    """Accessible inline SVG using query outputs, with a zero baseline."""
    config={
        '01':('onboarding_funnel','stage','users','Ordered onboarding reach (users)'),
        '02':('variant_summary','variant','conversion_rate','Observed conversion rate (proportion)'),
        '03':('funnel_by_segment','device','conversion_rate','Conversion by device and channel (proportion)'),
        '04':('category_performance','category','recorded_revenue','Recorded revenue by category'),
        '05':('stage_reach','journey_stage','users','Unordered stage reach (users; not a sequential funnel)')}
    table,label,value,title=config[key[:2]]
    frame=results[table].head(10)
    labels=frame[label].astype(str)
    if key.startswith('03'): labels=labels+' / '+frame.channel.astype(str)
    maximum=float(frame[value].max()) or 1
    height=65+len(frame)*43
    parts=[f'<svg viewBox="0 0 1000 {height}" role="img" aria-labelledby="chartTitle"><title id="chartTitle">{html.escape(title)}</title><text x="0" y="24" font-size="19" fill="#17283d">{html.escape(title)}</text>']
    for i,(label_,number) in enumerate(zip(labels,frame[value])):
        y=46+i*43;width=float(number)/maximum*520
        parts.append(f'<text x="0" y="{y+18}" font-size="14" fill="#17283d">{html.escape(label_)}</text><rect x="290" y="{y}" width="{width:.3f}" height="26" rx="3" fill="#087f8c"/><text x="{300+width:.3f}" y="{y+18}" font-size="14" fill="#17283d">{number:,.4g}</text>')
    parts.append('</svg>')
    return ''.join(parts)


def highlights(key, results, extra):
    if key.startswith('01'):
        row=results['summary'].iloc[0]
        return f"The supplied subscription snapshot totals {row.snapshot_mrr:,.2f} MRR across {int(row.paying_users):,} paying users. The paying-user churn label rate is {row.paying_churn_label_rate:.2%}. Ordered Step 1-to-Step 2 loss is {extra['onboarding_step2_conditional_dropoff']:.2%}; this is a descriptive funnel result, not a measured intervention outcome."
    if key.startswith('02'):
        e=extra['experiment']
        return f"Control converts at {e['control_rate']:.2%} and Variant B at {e['treatment_rate']:.2%}: +{e['absolute_lift']*100:.2f} percentage points, or {e['relative_lift']:.2%} relative lift. The unadjusted 95% difference interval is {e['difference_ci_low']*100:.2f} to {e['difference_ci_high']*100:.2f} percentage points. Statistical inference remains conditional on unverified session independence."
    if key.startswith('03'):
        row=results['summary'].iloc[0]
        return f"Observed session conversion is {row.conversion_rate:.2%}; cart abandonment is {row.cart_abandonment_rate:.2%}. The top 20% of SKUs contribute {extra['top_20_percent_sku_revenue_share']:.2%} of recorded order revenue. These outputs replace the earlier untraceable 68% concentration claim."
    if key.startswith('04'):
        row=results['summary'].iloc[0]
        return f"The source records {row.recorded_revenue:,.2f} in revenue across {int(row.sales_rows):,} sale rows. {int(row.revenue_discrepancy_rows):,} rows differ from price × units by more than 0.011. The top ten sellers contribute {extra['top_10_seller_revenue_share']:.2%}. The data do not establish platform commission revenue or order counts."
    row=results['summary'].iloc[0]
    return f"There are {int(row.purchasers):,} observed purchasers among {int(row.users):,} users ({row.observed_purchase_rate:.2%}). No user satisfies the entire six-step date-ordered path in the supplied records. This conflicts with purchase reach and signals source sequencing problems; it is not evidence of zero actual purchases or 100% business checkout abandonment."


def report(project, results, extra, quality, checks):
    title,question,action,limits=GUIDANCE[project.name[:2]]
    sections=[f'# {title}', '**Data provenance:** supplied simulated portfolio CSVs. No external client or production outcome is implied.',
              '## Decision question',question,'## Headline interpretation',highlights(project.name,results,extra),'## Computed findings']
    for name,frame in results.items():
        sections.extend([f'### {name.replace("_"," ").title()}',markdown_table(frame.head(10)),f'Full output: [Results/{name}.csv](Results/{name}.csv).'])
    sections.extend(['## Additional calculations','```json',json.dumps(extra,indent=2,allow_nan=False),'```',
                     '## Recommendation',action,'## Limits and assumptions',limits,
                     '## Reproduction','From the repository root: `python -m portfolio.run --project '+project.name+'`.',
                     'Each named query in `SQL/analysis.sql` writes a corresponding results CSV. The Python runner independently reconciles headline metrics and ordered funnels. See `Results/validation.json` for checks and `Results/quality.json` for source diagnostics.',
                     '## Existing BI workbooks','The original Power BI/Tableau dashboards are retained as separate-data legacy assets. The Excel summaries have been corrected. Native-file inspection confirms that the legacy Power BI/Tableau dashboards use different datasets. Corrected Excel summaries reconcile to the canonical CSVs; see the native verification report for engine-specific evidence. Use `Results/` and `REPORT.html` for the canonical analysis. See `Docs/Dashboard_Reconciliation.md` before presenting a legacy screenshot as evidence.',
                     '## Validation',f'{len(checks)} blocking checks passed. Source limitations remain documented; a passing technical check does not establish causal validity.'])
    text='\n\n'.join(sections)+'\n';(project/'README.md').write_text(text)
    html_sections=[f'<section><h2>What the data support</h2><p>{html.escape(highlights(project.name,results,extra))}</p>{chart(project.name,results)}</section>']
    for name,frame in results.items():
        html_sections.append(f'<section><h2>{html.escape(name.replace("_"," ").title())}</h2><div class="scroll">{frame.head(20).to_html(index=False,float_format=lambda x:f"{x:,.4f}",border=0)}</div><p><a href="Results/{name}.csv">Download complete result</a></p></section>')
    warnings=''.join(f'<li><b>{html.escape(i["issue"])}</b>: {i["affected_rows"]:,} rows. {html.escape(i["interpretation"])}</li>' for i in quality['semantic_issues'])
    document='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+html.escape(title)+'''</title><style>
body{margin:0;background:#f1f5f9;color:#17283d;font:16px/1.6 system-ui,sans-serif}main{max-width:1200px;margin:auto;padding:36px 24px}header{background:#102f47;color:white;padding:32px;border-radius:16px}h1{line-height:1.15;font-size:36px}h2{font-size:23px}section{background:white;padding:24px;margin:22px 0;border-radius:12px;border:1px solid #dce4ea}.tag{color:#8ee8d1;text-transform:uppercase;letter-spacing:.1em;font-size:13px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:10px;text-align:right;border-bottom:1px solid #e2e8f0}th{background:#edf4f8}td:first-child,th:first-child{text-align:left}.scroll{overflow:auto}a{color:#075985}pre{overflow:auto;white-space:pre-wrap}.note{border-left:5px solid #b7791f}li{margin:10px 0}@media print{body{background:white}main{padding:0}section{break-inside:avoid}header{color:#102f47;background:white}}
</style><main><header><div class="tag">Jamie Christian · Reproducible analysis</div><h1>'''+html.escape(title)+'''</h1><p>'''+html.escape(question)+'''</p><p>Simulated data · SQL + Python reconciliation · '''+str(len(checks))+''' passed checks</p></header>'''+''.join(html_sections)+f'<section><h2>Statistical and supplementary results</h2><pre>{html.escape(json.dumps(extra,indent=2))}</pre></section><section><h2>Recommended next decision</h2><p>{html.escape(action)}</p></section><section class="note"><h2>Interpretation limits</h2><p>{html.escape(limits)}</p><ul>{warnings}</ul></section><p>Generated from supplied CSVs. Legacy BI source mismatch documented; corrected Excel and replacement Hyper sources have separate verification evidence. <a href="README.md">Full case study</a></p></main></html>'
    (project/'REPORT.html').write_text(document)


def run_project(root,key):
    project=root/key;results_dir=project/'Results';results_dir.mkdir(exist_ok=True)
    # Invalidate prior success evidence before touching outputs. A failed run must
    # not leave a success manifest for its partially updated result set.
    for evidence in ('validation.json','manifest.json'):
        (results_dir/evidence).unlink(missing_ok=True)
    build=root/'build'/key;build.mkdir(parents=True,exist_ok=True)
    t={};quality={'tables':{},'semantic_issues':[]};checks=[];sources={}
    for name,(pk,spec) in PROJECTS[key].items():
        source=project/'Data'/'raw'/f'{name}_raw.csv';frame=pd.read_csv(source, float_precision='round_trip')
        clean=clean_table(frame,spec,pk);t[name]=clean
        path=project/'Data'/'clean'/f'{name}_clean.csv';path.parent.mkdir(exist_ok=True)
        clean.to_csv(path,index=False)
        quality['tables'][name]={'input_rows':len(frame),'output_rows':len(clean),'null_cells':int(frame.isna().sum().sum()),'exact_repeat_rows':int(frame.duplicated().sum()),'primary_key':pk,'duplicate_policy':'Primary key duplicates fail; repeated event/fact rows without stable event IDs are preserved.','source_sha256':digest(source),'clean_sha256':digest(path)}
        checks.append({'check':f'{name}: schema, types, ranges, required values and key','passed':True})
        sources[str(source.relative_to(root))]=digest(source)
    quality['semantic_issues']=validate_relations(key,t,checks)
    with sqlite3.connect(build/'analysis.sqlite') as connection:
        for name,frame in t.items():frame.to_sql(name+'_clean',connection,if_exists='replace',index=False)
        for name,(pk,_) in PROJECTS[key].items():
            if pk:connection.execute(f'CREATE UNIQUE INDEX IF NOT EXISTS idx_{name}_{pk} ON {name}_clean({pk})')
        # Recreate secondary indexes after pandas replaces each table.
        for name,frame in t.items():
            for col in ['user_id','listing_id']:
                if col in frame:connection.execute(f'CREATE INDEX IF NOT EXISTS ix_{name}_{col} ON {name}_clean({col})')
        output={}
        for name,sql in read_queries(project/'SQL'/'analysis.sql'):
            output[name]=pd.read_sql_query(sql,connection)
            output[name].to_csv(results_dir/(name+'.csv'),index=False,float_format='%.12g')
            checks.append({'check':f'SQL executed: {name}','passed':True})
        extra=reconcile(key,t,output,checks)
        plans={name:[list(row) for row in connection.execute('EXPLAIN QUERY PLAN '+sql)] for name,sql in read_queries(project/'SQL'/'analysis.sql')}
    write_json(results_dir/'quality.json',quality);write_json(results_dir/'validation.json',{'passed':True,'checks':checks})
    write_json(results_dir/'additional_metrics.json',extra);write_json(results_dir/'query_plans.json',plans)
    report(project,output,extra,quality,checks)
    versions={'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'pandas':pd.__version__,'numpy':np.__version__,'scipy':scipy.__version__}
    code_paths=sorted((root/'portfolio').glob('*.py'))+[project/'SQL'/'analysis.sql',root/'requirements.txt']
    manifest={'sources':sources,'code':{str(p.relative_to(root)):digest(p) for p in code_paths},'software':versions,
              'outputs':{str(p.relative_to(root)):digest(p) for p in sorted(list(results_dir.glob('*'))+list((project/'Data'/'clean').glob('*.csv'))+[project/'REPORT.html',project/'README.md']) if p.name!='manifest.json'},
              'check_count':len(checks),'project':key,'data_kind':'supplied simulated data'}
    write_json(results_dir/'manifest.json',manifest)
    return {'project':key,'checks':len(checks),'rows':sum(len(f) for f in t.values()),'passed':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--project',choices=list(PROJECTS))
    args=parser.parse_args();root=args.root.resolve()
    (root/'build'/'run_summary.json').unlink(missing_ok=True)
    summary=[run_project(root,key) for key in ([args.project] if args.project else PROJECTS)]
    (root/'build').mkdir(exist_ok=True)
    write_json(root/'build'/'run_summary.json',summary)
    for item in summary:print(f"PASS {item['project']}: {item['checks']} checks; {item['rows']:,} source rows")

if __name__=='__main__':main()
