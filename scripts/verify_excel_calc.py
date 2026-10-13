"""Verify XLSX formulas using LibreOffice Calc with all formula caches cleared.

Read-only to delivered workbooks: creates disposable copies and invokes Calc.
Requires `soffice` plus optional native requirements. Native Microsoft Excel
is a different engine and is not claimed as executed.
"""
from pathlib import Path
import argparse,hashlib,json,math,subprocess,tempfile,zipfile,xml.etree.ElementTree as ET
from openpyxl import load_workbook
ROOT=Path(__file__).resolve().parents[1]
NS={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def clear_formula_caches(source,destination):
 """Test instrumentation only; never changes formula logic or final workbook."""
 with zipfile.ZipFile(source) as z,zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as out:
  for item in z.infolist():
   content=z.read(item.filename)
   if item.filename.startswith('xl/worksheets/') and item.filename.endswith('.xml'):
    tree=ET.fromstring(content)
    for cell in tree.findall('.//x:c',NS):
     if cell.find('x:f',NS) is not None:
      value=cell.find('x:v',NS)
      if value is not None:cell.remove(value)
    content=ET.tostring(tree,encoding='utf-8',xml_declaration=True)
   out.writestr(item,content)

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--mutation-dir',type=Path);args=parser.parse_args()
 evidence=json.loads((ROOT/'verification/native/excel_formula_verification.json').read_text());results=[]
 version=subprocess.check_output(['soffice','--version'],text=True).strip()
 with tempfile.TemporaryDirectory(prefix='excel-calc-') as tmp:
  base=Path(tmp);source_dir=base/'input';target=base/'output';source_dir.mkdir();target.mkdir()
  tasks=[]
  for e in evidence:
   original=ROOT/e['workbook'];name=original.name
   clear_formula_caches(original,source_dir/name);tasks.append((e,False,name))
   if args.mutation_dir:
    mutated=args.mutation_dir/name
    if not mutated.exists():raise FileNotFoundError(mutated)
    name='mutation_'+name;clear_formula_caches(mutated,source_dir/name);tasks.append((e,True,name))
  command=['soffice',f'-env:UserInstallation={(base/"profile").as_uri()}','--headless','--convert-to','xlsx','--outdir',str(target)]+[str(source_dir/name) for _,_,name in tasks]
  result=subprocess.run(command,text=True,capture_output=True,timeout=240)
  if result.returncode:raise RuntimeError(result.stderr)
  for e,mutated,name in tasks:
   output=target/name
   if not output.exists():raise RuntimeError(f'No Calc output for {name}: {result.stdout} {result.stderr}')
   w=load_workbook(output,data_only=True,read_only=True);checks=[]
   expected=e['summary_cells'] if not mutated else [{'cell':e['mutation']['result_cell'],'expected':e['mutation']['baseline']+e['mutation']['expected_delta']}]
   for item in expected:
    value=w['Summary'][item['cell']].value;want=item['expected'];passed=isinstance(value,(int,float)) and math.isfinite(value) and abs(value-want)<=max(1e-8,abs(want)*1e-10)
    checks.append({'cell':item['cell'],'expected':want,'observed':value,'passed':passed})
   errors=[]
   for sheet in w:
    for row in sheet:
     for cell in row:
      if cell.data_type=='e':errors.append(f'{sheet.title}!{cell.coordinate}: {cell.value}')
   w.close()
   entry={'workbook':e['workbook'],'sha256':hashlib.sha256((ROOT/e['workbook']).read_bytes()).hexdigest(),'engine':version,'formula_caches_removed_before_open':True,'source_perturbation_copy':mutated,'checks':checks,'formula_errors':errors,'passed':all(c['passed'] for c in checks) and not errors}
   results.append(entry)
   print(e['project'],'mutation' if mutated else 'baseline',entry['passed'])
   if not entry['passed']:raise AssertionError(entry)
 (ROOT/'verification/native/excel_calc_verification.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':main()
