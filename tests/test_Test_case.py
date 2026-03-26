from pages.Ts_case_page import TS_case_page



def test_ts_page(home_page):
    test_page = TS_case_page(home_page)
    test_page.ts_page()

