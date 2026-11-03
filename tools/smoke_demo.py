#!/usr/bin/env python3
"""Offline Chromium smoke test for the five-project analytics explorer.

Checks interactive behavior, keyboard navigation, mobile overflow and runtime
JavaScript errors. This is not an accessibility certification or native BI test.
"""
from __future__ import annotations

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo" / "analytics-explorer.html"
REPORTS = ROOT / "reports"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    REPORTS.mkdir(exist_ok=True)
    errors: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        page.route("http://**/*", lambda route: route.abort())
        page.route("https://**/*", lambda route: route.abort())
        page.goto(DEMO.as_uri(), wait_until="load")
        check(page.title().startswith("Analytics Explorer"), "Missing dashboard title")
        check(page.locator("#project option").count() == 5, "Must expose five projects")
        check(page.locator("#bars .bar-row").count() == 5, "Default SaaS bars missing")
        page.screenshot(path=str(REPORTS / "analytics-desktop.png"), full_page=True)
        page.select_option("#project", "1")
        check(page.locator("#metric option").count() >= 2, "Experiment metric switch failed")
        check(page.locator("#bars .bar-row").count() == 2, "Experiment rows incorrect")
        page.fill("#search", "UNMATCHED-SMOKE-SEARCH")
        check(page.get_by_text("No rows match this search.").count() == 1,
              "No-results state missing")
        page.fill("#search", "")
        page.select_option("#project", "2")
        page.select_option("#limit", "all")
        check(page.locator("#bars .bar-row").count() == 10, "Ecommerce rows incomplete")
        page.locator("#project").focus()
        page.keyboard.press("Tab")
        check(page.evaluate("document.activeElement.id") == "metric",
              "Keyboard navigation between filters failed")
        page.set_viewport_size({"width": 390, "height": 844})
        page.screenshot(path=str(REPORTS / "analytics-mobile.png"), full_page=True)
        overflowing = page.evaluate(
            "document.documentElement.scrollWidth > window.innerWidth + 2"
        )
        check(not overflowing, "Mobile horizontal overflow")
        check(not errors, "Runtime errors: " + "; ".join(errors))
        browser.close()
    print("PASS: default chart, switching, filtering, keyboard, mobile, no JS errors")


if __name__ == "__main__":
    main()
