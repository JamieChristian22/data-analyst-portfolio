"""Verify the published offline explorer against the checked-in analytics evidence.

No runtime network, cloud account or native BI software is required.
"""
import csv
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "demo/analytics-explorer.html"

class ExplorerEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = HTML.read_text(encoding="utf-8")
        match = re.search(
            r'<script id="portfolio-data" type="application/json">(.*?)</script>',
            cls.page, flags=re.DOTALL,
        )
        if match is None:
            raise AssertionError("Source-backed embedded JSON was not found")
        cls.data = json.loads(match.group(1))

    def test_five_projects_have_unmodified_source_rows(self):
        datasets = self.data["datasets"]
        self.assertEqual(len(datasets), 5)
        self.assertEqual(len({d["path"] for d in datasets}), len(datasets))
        for item in datasets:
            with self.subTest(source=item["path"]):
                path = ROOT / item["path"]
                self.assertTrue(path.is_file())
                with path.open(newline="", encoding="utf-8") as source:
                    canonical = list(csv.DictReader(source))
                self.assertEqual(item["rows"], canonical)
                self.assertTrue(canonical, "A demo must not claim nonexistent data")
                label_fields = item["label"] if isinstance(item["label"], list) else [item["label"]]
                self.assertTrue(set(label_fields).issubset(canonical[0]))
                self.assertTrue(set(item["metrics"]).issubset(canonical[0]))
                for row in canonical:
                    for field in item["metrics"]:
                        self.assertGreaterEqual(float(row[field]), 0)
                project = item["path"].split("/", 1)[0]
                verification = json.loads((ROOT / project / "Results/validation.json").read_text())
                self.assertTrue(verification["passed"])
                self.assertTrue(all(check["passed"] for check in verification["checks"]))

    def test_accessible_controls_and_safe_offline_rendering(self):
        for control in ("project", "metric", "search", "sort", "limit"):
            self.assertIn('for="' + control + '"', self.page)
            self.assertIn('id="' + control + '"', self.page)
        self.assertIn('aria-live="polite"', self.page)
        self.assertIn("textContent", self.page)
        self.assertIn('role="group"', self.page)
        self.assertNotIn("innerHTML", self.page)
        self.assertNotIn("document.write", self.page)
        self.assertIsNone(re.search(r'<script[^>]+src=', self.page, flags=re.I))
        self.assertIsNone(re.search(r'<link[^>]+href=', self.page, flags=re.I))
        self.assertNotIn("fetch(", self.page)

    def test_browser_does_not_silently_replace_invalid_metrics_with_zero(self):
        self.assertIn('throw new Error("Invalid chart metric: "+key)', self.page)
        self.assertNotIn('Number.isFinite(val)?val:0', self.page)

    def test_limitations_for_experiment_and_unordered_journey_are_explicit(self):
        datasets = {item["category"]: item for item in self.data["datasets"]}
        self.assertIn("independence", datasets["Experiment"]["note"])
        self.assertIn("Unordered", datasets["Journey"]["note"])
        self.assertIn("synthetic", self.data["scope"])
