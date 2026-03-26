from playwright.sync_api import expect


class TS_case_page():

    def __init__(self,page):
        self.page = page

    def ts_page(self):
        test_page = self.page.locator("li", has_text="Test Cases")
        expect(test_page).to_be_visible()
        test_page.click()

