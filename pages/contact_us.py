from playwright.sync_api import expect
from playwright.sync_api import Page, expect


class contact_us:

    def __init__(self, page):
        self.page = page
        self.navigation_click =  page.get_by_role("link", name = "Contact us")



    def navigate_contact_page(self):
       self.navigation_click.click()
       expect(self.page.get_by_text("Get In Touch")).to_be_visible()

       self.page.get_by_placeholder("Name").fill("Gollal")
       self.page.locator("input[data-qa='email']").fill("gollal009@gmail.com")

       subject = self.page.locator("input[data-qa='subject']")
       expect(subject).to_be_visible()
       subject.fill("djbsjdb")

       self.page.locator("#message").fill("djbsjdb")

       self.page.on("dialog",lambda dialog:dialog.accept())
       self.page.get_by_role("button", name = "Submit").click()
       self.page.wait_for_timeout(10000)

       success = self.page.locator(".status.alert-success")
       expect(success).to_be_visible(timeout=10000)

       self.page.locator(".btn-success").click()












