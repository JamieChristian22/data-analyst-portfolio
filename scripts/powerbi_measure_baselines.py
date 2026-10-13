"""Compute independent expectations from decoded legacy PBIX data.

Generates DAX Query View tests but does not claim to execute those tests.
The embedded sources are a separate dataset from the canonical CSV projects.
"""
from pathlib import Path
import json,hashlib
from pbixray import PBIXRay
ROOT=Path(__file__).resolve().parents[1]
def main():
 for project in sorted(ROOT.glob('0[34]_*')):
  p=next((project/'Dashboard').glob('*.pbix'));m=PBIXRay(str(p));out=ROOT/'verification/native'/project.name
  if project.name.startswith('03'):
   payments=m.get_table('payments');orders=m.get_table('orders');events=m.get_table('sessions')
   expected={'Total Revenue':float(payments.revenue_usd.sum()),'Total Orders':int(orders.order_id.nunique())}
   expected['AOV']=expected['Total Revenue']/expected['Total Orders']
   prefixes=[('Product Views','view_product'),('Add To Cart','add_to_cart'),('Checkouts','checkout'),('Purchases (Events)','purchase')]
   for measure,event in prefixes:expected[measure]=int(events.loc[events.event_type.eq(event),'session_id'].nunique())
   sets=[set(events.loc[events.event_type.eq(event),'customer_id'].dropna()) for _,event in prefixes]
   cumulative=sets[0]
   for name,s in zip(['Viewed Customers','Cart Customers','Checkout Customers','Purchased Customers'],sets):
    cumulative=cumulative&s;expected[name]=len(cumulative)
  else:
   orders=m.get_table('fact_orders')
   expected={name:float(orders[col].sum()) for name,col in [('GMV','GrossRevenue'),('Units Sold','Units'),('Marketplace Revenue','MarketplaceFee'),('Fulfillment Cost','FulfillmentCost'),('Net Seller Revenue','NetSellerRevenue')]}
   expected['Orders']=int(orders.OrderID.nunique());expected['AOV']=expected['GMV']/expected['Orders'];expected['Take Rate %']=expected['Marketplace Revenue']/expected['GMV']
  available=set(m.dax_measures.Name);expected={name:value for name,value in expected.items() if name in available}
  lines=['// Execute in Power BI Desktop DAX Query View on this original PBIX.','// This query was GENERATED, not executed in this environment.','// Each calculation removes report filter context by running as a standalone query.','EVALUATE','UNION(']
  clauses=[]
  for name,value in expected.items():
   tolerance=1e-8 if '%' in name else .01
   clauses.append(f'    ROW("Metric", "{name}", "Actual", [{name}], "Expected", {value:.12g}, "Tolerance", {tolerance}, "Passed", ABS([{name}] - {value:.12g}) <= {tolerance})')
  lines.append(',\n'.join(clauses));lines.append(')')
  (out/'verify_legacy_measures.dax').write_text('\n'.join(lines)+'\n')
  (out/'powerbi_measure_baselines.json').write_text(json.dumps({'pbix':str(p.relative_to(ROOT)),'pbix_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'baseline_engine':'PBIXRay decode + independent Python aggregation','dax_execution':'NOT_RUN','expected_unfiltered_measures':expected},indent=2)+'\n')
  print(project.name,len(expected),'measure baselines')
if __name__=='__main__':main()
