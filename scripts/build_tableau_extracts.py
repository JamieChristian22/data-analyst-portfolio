"""Build and verify Tableau-native extracts for the three Tableau projects.

These are source-aligned replacement DATA SOURCES, not rebuilt .twbx dashboards.
Every source/result cell is read back through the Hyper engine and compared.
"""
from pathlib import Path
import hashlib,json,tempfile
import numpy as np
import pandas as pd
from tableauhyperapi import HyperProcess,Connection,Telemetry,CreateMode,TableDefinition,TableName,SqlType,Inserter
ROOT=Path(__file__).resolve().parents[1]

def main():
 evidence=[]
 with tempfile.TemporaryDirectory(prefix='hyper-build-') as log:
  for project in sorted(ROOT.glob('0[125]_*')):
   with HyperProcess(Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU,parameters={'log_dir':log,'use_tcp_port':'auto'}) as process:
    path=project/'Dashboard/Validated_Analysis.hyper';checks=[]
    with Connection(process.endpoint,str(path),CreateMode.CREATE_AND_REPLACE) as c:
     for schema,folder in [('Source',project/'Data/clean'),('Results',project/'Results')]:
      c.catalog.create_schema(schema)
      for csv in sorted(folder.glob('*.csv')):
       frame=pd.read_csv(csv,float_precision='round_trip');types=[]
       for col in frame:
        kind=SqlType.big_int() if pd.api.types.is_integer_dtype(frame[col]) else SqlType.double() if pd.api.types.is_numeric_dtype(frame[col]) else SqlType.text()
        types.append(TableDefinition.Column(col,kind))
       table=TableName(schema,csv.stem);definition=TableDefinition(table,types)
       c.catalog.create_table(definition)
       rows=[[None if pd.isna(v) else v for v in row] for row in frame.itertuples(index=False,name=None)]
       with Inserter(c,definition) as inserter:inserter.add_rows(rows);inserter.execute()
       observed=pd.DataFrame(c.execute_list_query(f'SELECT * FROM {table}'),columns=frame.columns)
       # Compare multisets of rows, not an incidental database scan order.
       def normalized(data):
        result=data.copy()
        for col in frame:
         if pd.api.types.is_numeric_dtype(frame[col]):result[col]=pd.to_numeric(result[col]).astype(float).round(8)
         else:result[col]=result[col].fillna('<NULL>').astype(str)
        return result.sort_values(list(result.columns)).reset_index(drop=True)
       pd.testing.assert_frame_equal(normalized(observed),normalized(frame),check_dtype=False,check_exact=False,rtol=1e-10,atol=1e-8)
       checks.append({'table':str(table),'rows':len(frame),'all_cells_match':True,'csv':str(csv.relative_to(ROOT)),'csv_sha256':hashlib.sha256(csv.read_bytes()).hexdigest()})
    evidence.append({'file':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'engine':'Tableau Hyper API 0.0.26784','checks':checks,'tableau_desktop_dashboard_refresh':'NOT_RUN'})
    print(project.name,len(checks),'native tables verified')
 (ROOT/'verification/native/tableau_extract_verification.json').write_text(json.dumps(evidence,indent=2)+'\n')
if __name__=='__main__':main()
