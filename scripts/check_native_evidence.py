"""Check native evidence integrity without mistaking partial verification for certification."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'verification/native'
def read(name):return json.loads((BASE/name).read_text())
def matching(path,expected):
 actual=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
 if actual!=expected:raise AssertionError(f'Stale evidence: {path}')
def main():
 audit=read('workbook_audit.json');calc=read('excel_calc_verification.json');extracts=read('tableau_extract_verification.json')
 for asset in audit:matching(asset['file'],asset['sha256'])
 for entry in calc:
  matching(entry['workbook'],entry['sha256'])
  if not entry['passed'] or not entry['formula_caches_removed_before_open']:raise AssertionError('Unverified spreadsheet calculation')
 for extract in extracts:
  matching(extract['file'],extract['sha256'])
  for check in extract['checks']:
   matching(check['csv'],check['csv_sha256'])
   if not check['all_cells_match']:raise AssertionError('Extract value mismatch')
 for project in ROOT.glob('0[1-5]_*'):
  manifest=json.loads((project/'Results/manifest.json').read_text())
  for path,hash_ in {**manifest['sources'],**manifest['outputs'],**manifest['code']}.items():matching(path,hash_)
 relation=read('canonical_relationship_checks.json');matching(relation['source'],relation['sha256'])
 if not relation['passed']:raise AssertionError('Journey COUNTIF grain is not valid')
 report={'evidence_integrity':'PASS','overall_native_dashboard_certification':'NOT_CERTIFIED',
 'excel_workbooks_with_baseline_recalculation':sum(not x['source_perturbation_copy'] for x in calc),
 'excel_workbooks_with_perturbation_recalculation':sum(x['source_perturbation_copy'] for x in calc),
 'excel_summary_formulas_checked':sum(len(x['checks']) for x in calc if not x['source_perturbation_copy']),
 'replacement_hyper_tables_verified':sum(len(x['checks']) for x in extracts),
 'legacy_dashboard_source_mismatches':sum(x.get('source_reconciliation')=='MISMATCH' for x in audit),
 'remaining':['Legacy BI dashboards must be rebuilt against canonical sources or presented as separate-data case studies.','Power BI Desktop DAX evaluation and Tableau Desktop refresh/render are not executed.','Microsoft Excel-specific recalculation is not executed; Artifact Tool and desktop Calc were checked.']}
 (BASE/'SUMMARY.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
