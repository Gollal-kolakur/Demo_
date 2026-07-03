from pages.ts_case_page import TS_case_page



def test_ts_page(browser_page):
    test_page = TS_case_page(browser_page)
    test_page.ts_page()

