"""Exercise real SQL on controlled edge cases and committed outputs."""
import json
import sqlite3
import unittest
from pathlib import Path
import pandas as pd
from portfolio.run import read_queries
from portfolio.contracts import PROJECTS

ROOT=Path(__file__).resolve().parents[1]
class SQLTests(unittest.TestCase):
    def test_empty_cart_denominator_is_null(self):
        p=ROOT/'03_Ecommerce_Product_Analytics'
        query=dict(read_queries(p/'SQL/analysis.sql'))['funnel_by_segment']
        with sqlite3.connect(':memory:') as c:
            pd.DataFrame({'device':['Mobile'],'channel':['Paid'],'added_to_cart':[0],'purchased':[0]}).to_sql('web_sessions_clean',c,index=False)
            row=c.execute(query).fetchone()
        self.assertIsNone(row[-1]);self.assertEqual(row[-2],0)
    def test_sql_funnel_retry_semantics(self):
        p=ROOT/'05_User_Journey_Analytics'
        query=dict(read_queries(p/'SQL/analysis.sql'))['ordered_funnel']
        with sqlite3.connect(':memory:') as c:
            pd.DataFrame({'user_id':[1],'first_seen_date':['2025-01-01']}).to_sql('users_clean',c,index=False)
            pd.DataFrame([(1,'2025-01-03','Landing'),(1,'2025-01-02','Browse'),(1,'2025-01-04','Browse')],columns=['user_id','event_date','journey_stage']).to_sql('journey_events_clean',c,index=False)
            rows=c.execute(query).fetchall()
        self.assertEqual([r[2] for r in rows],[1,1,0,0,0,0])
    def test_sku_rounds_up_top_twenty_percent(self):
        query=dict(read_queries(ROOT/'03_Ecommerce_Product_Analytics/SQL/analysis.sql'))['sku_pareto']
        with sqlite3.connect(':memory:') as c:
            pd.DataFrame({'sku':list('ABCDEF'),'order_value':[60,50,40,30,20,10]}).to_sql('orders_clean',c,index=False)
            result=pd.read_sql_query(query,c)
        self.assertEqual(result.in_top_20_percent.sum(),2)
        self.assertEqual(result.iloc[0].sku,'A')
    def test_every_project_has_passing_validation(self):
        for name in PROJECTS:
            with self.subTest(project=name):
                evidence=json.loads((ROOT/name/'Results/validation.json').read_text())
                self.assertTrue(evidence['passed']);self.assertTrue(all(c['passed'] for c in evidence['checks']))
    def test_results_match_manifest(self):
        import hashlib
        for name in PROJECTS:
            m=json.loads((ROOT/name/'Results/manifest.json').read_text())
            for path,digest in {**m['sources'],**m['outputs'],**m['code']}.items():
                with self.subTest(path=path):self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)
