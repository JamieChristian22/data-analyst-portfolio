"""Verify a CSV exported from the generated DAX Query View verification query.

Example: python scripts/verify_powerbi_export.py --project 03 --csv dax-output.csv
Does not treat the CSV's own Passed column as evidence. Rechecks every metric
against the independently derived embedded-data baseline and current PBIX hash.
"""
import argparse,csv,hashlib,json,math,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def validate_rows(rows,expected):
 normalized=[{k.strip('[]'):v for k,v in row.items()} for row in rows]
 names=[r.get('Metric') for r in normalized]
 if len(names)!=len(set(names)) or set(names)!=set(expected):raise ValueError('Missing, duplicate or unexpected metric')
 checks=[]
 for row in normalized:
  name=row['Metric'];actual=float(row['Actual']);target=float(expected[name]);tolerance=1e-8 if '%' in name else .01
  if not math.isfinite(actual):raise ValueError('Nonfinite actual')
  checks.append({'metric':name,'actual':actual,'expected':target,'tolerance':tolerance,'passed':abs(actual-target)<=tolerance})
 return checks

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--project',choices=['03','04'],required=True);p.add_argument('--csv',type=Path,required=True);args=p.parse_args()
 project=next(ROOT.glob(args.project+'_*'));folder=ROOT/'verification/native'/project.name
 baseline=json.loads((folder/'powerbi_measure_baselines.json').read_text());workbook=ROOT/baseline['pbix']
 if hashlib.sha256(workbook.read_bytes()).hexdigest()!=baseline['pbix_sha256']:raise ValueError('Workbook changed; regenerate baselines before acceptance')
 with args.csv.open(newline='',encoding='utf-8-sig') as f:checks=validate_rows(list(csv.DictReader(f)),baseline['expected_unfiltered_measures'])
 # A user-supplied exported file is evidence of reported Desktop output, not
 # independent attestation that this environment executed the Desktop engine.
 result={'evidence_origin':'user-supplied DAX Query View CSV','pbix_sha256':baseline['pbix_sha256'],'csv_sha256':hashlib.sha256(args.csv.read_bytes()).hexdigest(),'passed':all(c['passed'] for c in checks),'checks':checks}
 folder.mkdir(exist_ok=True);(folder/'desktop_export_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 shutil.copyfile(args.csv,folder/'desktop_export.csv')
 if not result['passed']:raise SystemExit('Metric verification failed')
 print('Exported results match all independent baselines. Desktop rendering and refresh remain separate checks.')
if __name__=='__main__':main()
