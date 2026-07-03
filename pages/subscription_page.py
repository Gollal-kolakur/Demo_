from playwright.sync_api import expect

class subscription_page():

    def __init__(self,page):
        self.page = page

    def subscription(self, success=None):
        element = self.page.get_by_text("Subscription")
        element.scroll_into_view_if_needed()
        expect(element).to_be_visible()
        self.page.get_by_placeholder("Your email address").fill("Test@gmail.com")
        self.page.locator("#subscribe").click()

