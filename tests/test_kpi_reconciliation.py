"""Independent cross-table KPI reconciliation using committed and regenerated results."""
import csv
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def records(project, name):
    path = ROOT / project / "Results" / (name + ".csv")
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def first(project, name="summary"):
    return records(project, name)[0]

class PortfolioKPIReconciliation(unittest.TestCase):
    def test_saas_revenue_and_ordered_onboarding(self):
        p = "01_SaaS_Product_Analytics_StreamFlow"
        s = first(p)
        reach = records(p, "onboarding_funnel")
        self.assertAlmostEqual(float(s["snapshot_arr"]), float(s["snapshot_mrr"]) * 12, places=4)
        self.assertGreaterEqual(int(s["users"]), int(s["paying_users"]))
        counts = [int(row["users"]) for row in reach]
        self.assertTrue(all(a >= b for a, b in zip(counts, counts[1:])))
        self.assertLessEqual(counts[0], int(s["users"]))

    def test_ab_variant_fractions_agree_with_counts(self):
        p = "02_AB_Test_Feature_Impact"
        arms = records(p, "variant_summary")
        self.assertEqual({row["variant"] for row in arms}, {"Control", "Variant B"})
        self.assertEqual(sum(int(row["sessions"]) for row in arms), 12000)
        for row in arms:
            n, successes = int(row["sessions"]), int(row["conversions"])
            self.assertLessEqual(successes, n)
            self.assertTrue(math.isclose(successes / n, float(row["conversion_rate"]), abs_tol=1e-10))
            self.assertTrue(math.isclose(float(row["revenue"]) / n,
                                         float(row["revenue_per_session"]), abs_tol=1e-9))

    def test_ecommerce_segment_totals_match_summary(self):
        p = "03_Ecommerce_Product_Analytics"
        summary = first(p)
        segments = records(p, "funnel_by_segment")
        for key, total in (("sessions", "sessions"), ("carts", "cart_sessions"), ("purchases", "purchases")):
            self.assertEqual(sum(int(row[key]) for row in segments), int(summary[total]))
        self.assertAlmostEqual(
            sum(int(row["purchases"]) for row in segments) / sum(int(row["sessions"]) for row in segments),
            float(summary["conversion_rate"]), places=10)
        self.assertAlmostEqual(
            1 - sum(int(row["purchases"]) for row in segments) / sum(int(row["carts"]) for row in segments),
            float(summary["cart_abandonment_rate"]), places=10)

    def test_marketplace_category_totals_match_recorded_revenue(self):
        p = "04_Amazon_Marketplace_Analytics"
        summary = first(p)
        categories = records(p, "category_performance")
        self.assertEqual(sum(int(row["units"]) for row in categories), int(summary["units"]))
        self.assertEqual(sum(int(row["sales_rows"]) for row in categories), int(summary["sales_rows"]))
        self.assertAlmostEqual(sum(float(row["recorded_revenue"]) for row in categories),
                               float(summary["recorded_revenue"]), places=2)

    def test_journey_reach_is_not_misrepresented_as_ordered_funnel(self):
        p = "05_User_Journey_Analytics"
        summary = first(p)
        stage = {row["journey_stage"]: int(row["users"]) for row in records(p, "stage_reach")}
        ordered = records(p, "ordered_funnel")
        self.assertEqual(stage["Landing"], int(summary["users"]))
        self.assertEqual(stage["Purchase"], int(summary["purchasers"]))
        self.assertAlmostEqual(stage["Purchase"] / stage["Landing"],
                               float(summary["observed_purchase_rate"]), places=10)
        # Ordered purchase completion may be lower than unordered purchase reach.
        self.assertLessEqual(int(ordered[-1]["users"]), stage["Purchase"])
