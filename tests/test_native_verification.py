import importlib.util,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('verify',Path(__file__).resolve().parents[1]/'scripts/verify_powerbi_export.py');verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)
class NativeEvidenceTests(unittest.TestCase):
 def test_exported_pass_flag_is_not_trusted(self):
  checks=verify.validate_rows([{'Metric':'Revenue','Actual':'9','Passed':'True'}],{'Revenue':10})
  self.assertFalse(checks[0]['passed'])
 def test_missing_metric_fails(self):
  with self.assertRaises(ValueError):verify.validate_rows([],{'Revenue':10})
 def test_duplicate_metric_fails(self):
  with self.assertRaises(ValueError):verify.validate_rows([{'Metric':'Revenue','Actual':'10'}]*2,{'Revenue':10})
 def test_bracketed_headers_and_tolerance(self):
  self.assertTrue(verify.validate_rows([{'[Metric]':'Revenue','[Actual]':'10.005'}],{'Revenue':10})[0]['passed'])
 def test_nan_fails(self):
  with self.assertRaises(ValueError):verify.validate_rows([{'Metric':'Revenue','Actual':'nan'}],{'Revenue':10})
