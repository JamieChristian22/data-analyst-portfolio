import unittest
import pandas as pd
from portfolio.quality import clean_table,foreign_key,ordered_funnel

class ContractTests(unittest.TestCase):
    def test_valid_normalization(self):
        f=pd.DataFrame({'id':[1],'flag':['True'],'label':[' A '],'date':['2025-01-01']})
        c=clean_table(f,'id:i flag:b label:s date:d','id')
        self.assertEqual(c.flag.iloc[0],1);self.assertEqual(c.label.iloc[0],'A')
    def test_missing_column(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'id':[1]}),'id:i value:f')
    def test_missing_value(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'value':[None]}),'value:f')
    def test_invalid_boolean(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'flag':[2]}),'flag:b')
    def test_nonfinite(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'value':[float('inf')]}),'value:f')
    def test_negative_money(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'value':[-2]}),'value:f')
    def test_fractional_key(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'user_id':[1.2]}),'user_id:i')
    def test_duplicate_primary_key(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'user_id':[1,1]}),'user_id:i','user_id')
    def test_ambiguous_event_duplicates_preserved(self):
        c=clean_table(pd.DataFrame({'user_id':[1,1]}),'user_id:i')
        self.assertEqual(len(c),2)
    def test_orphan_relationship(self):
        with self.assertRaises(ValueError):foreign_key(pd.DataFrame({'user_id':[2]}),pd.DataFrame({'user_id':[1]}),'user_id')
    def test_invalid_date(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'date':['2025-02-30']}),'date:d')
    def test_bad_rating(self):
        with self.assertRaises(ValueError):clean_table(pd.DataFrame({'rating':[7]}),'rating:f')

class FunnelTests(unittest.TestCase):
    def setUp(self):
        self.users=pd.DataFrame({'user_id':[1,2,3],'start':['2025-01-01']*3})
    def test_retries_same_day_and_out_of_order(self):
        e=pd.DataFrame([(1,'2025-01-02','A'),(1,'2025-01-01','B'),(1,'2025-01-03','B'),(2,'2025-01-02','A'),(2,'2025-01-02','B'),(3,'2025-01-03','A'),(3,'2025-01-02','B')],columns=['user_id','event_date','stage'])
        self.assertEqual(ordered_funnel(self.users,e,['A','B'],'stage','start'),[3,2])
    def test_missing_earlier_stage_not_conversion(self):
        e=pd.DataFrame([(1,'2025-01-02','B')],columns=['user_id','event_date','stage'])
        self.assertEqual(ordered_funnel(self.users,e,['A','B'],'stage','start'),[0,0])
    def test_pre_observation_event_excluded(self):
        e=pd.DataFrame([(1,'2024-12-31','A')],columns=['user_id','event_date','stage'])
        self.assertEqual(ordered_funnel(self.users,e,['A'],'stage','start'),[0])
