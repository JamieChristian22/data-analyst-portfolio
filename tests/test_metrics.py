import unittest
from portfolio.metrics import proportion_interval, experiment, ratio

class StatisticalTests(unittest.TestCase):
    def test_wilson_known_reference(self):
        low,high=proportion_interval(50,100)
        self.assertAlmostEqual(low,0.4038315,places=6)
        self.assertAlmostEqual(high,0.5961685,places=6)
    def test_zero_events_interval_has_upper_uncertainty(self):
        low,high=proportion_interval(0,100)
        self.assertAlmostEqual(low,0)
        self.assertGreater(high,0.03)
    def test_all_events_interval_has_lower_uncertainty(self):
        low,high=proportion_interval(100,100)
        self.assertLess(low,.97);self.assertAlmostEqual(high,1)
    def test_invalid_counts(self):
        for args in [(1,0),(-1,10),(11,10)]:
            with self.subTest(args=args),self.assertRaises(ValueError):proportion_interval(*args)
    def test_equal_arms_no_effect(self):
        r=experiment(20,100,20,100)
        self.assertEqual(r['p_value'],1)
        self.assertLess(r['difference_ci_low'],0);self.assertGreater(r['difference_ci_high'],0)
    def test_arm_swap_reverses_effect_not_pvalue(self):
        a=experiment(20,100,40,100);b=experiment(40,100,20,100)
        self.assertAlmostEqual(a['absolute_lift'],-b['absolute_lift'])
        self.assertAlmostEqual(a['difference_ci_low'],-b['difference_ci_high'])
        self.assertEqual(a['p_value'],b['p_value'])
    def test_zero_control_relative_lift_undefined(self):
        self.assertIsNone(experiment(0,100,10,100)['relative_lift'])
    def test_all_zero_no_numerical_failure(self):
        self.assertEqual(experiment(0,100,0,100)['p_value'],1)
    def test_severe_sample_ratio_mismatch(self):
        self.assertLess(experiment(20,100,2,10)['srm_p_value_50_50'],.001)

    def test_fractional_boolean_and_nonfinite_counts_are_rejected(self):
        for value in (1.5, True, float('nan'), float('inf'), '1'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                proportion_interval(value, 100)
        for value in (10.5, False, float('nan')):
            with self.subTest(value=value), self.assertRaises(ValueError):
                experiment(2, 20, 2, value)

    def test_invalid_confidence_levels_are_rejected(self):
        for confidence in (0, 1, -0.1, 1.1, float('nan'), float('inf'), True):
            with self.subTest(confidence=confidence), self.assertRaises(ValueError):
                proportion_interval(5, 20, confidence)

    def test_planned_unequal_allocation_distinguishes_srm_from_50_50(self):
        result = experiment(20, 100, 40, 200, expected_treatment_share=2/3)
        self.assertAlmostEqual(result['srm_p_value_expected_allocation'], 1)
        self.assertLess(result['srm_p_value_50_50'], 0.001)
        self.assertEqual(result['expected_treatment_share'], 2/3)
        self.assertAlmostEqual(result['absolute_lift'], 0)

    def test_invalid_planned_allocation_is_rejected(self):
        for share in (0, 1, -0.1, float('nan'), float('inf'), True):
            with self.subTest(share=share), self.assertRaises(ValueError):
                experiment(5, 10, 5, 10, expected_treatment_share=share)

    def test_safe_ratio(self):
        self.assertIsNone(ratio(1,0));self.assertEqual(ratio(1,4),.25)
