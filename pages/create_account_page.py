
from playwright.sync_api import Playwright, expect
import pytest




class create_account:


    def __init__(self ,page):
        self.page = page


    def create_account_details(self):
        self.page.wait_for_load_state("load")
        self.page.get_by_label("Mr.").check()
        expect(self.page.locator("input[data-qa='name']")).not_to_have_value("")
        password_field = (self.page.locator("input[data-qa='password']"))
        expect(password_field).to_be_visible()
        password_field.fill("Test@1234")
        expect(password_field).to_have_value("Test@1234")
        newsletter_checkbox = self.page.get_by_label("Sign up for our newsletter!")
        newsletter_checkbox.check()
        expect(newsletter_checkbox).to_be_checked()
        offer_checkbox = self.page.get_by_label("Receive special offers from our partners!")
        offer_checkbox.check()
        expect(offer_checkbox).to_be_checked()
        self.page.select_option("#days", "10")
        self.page.select_option("#months", "5")
        self.page.select_option("#years", "1995")
        self.page.check("#newsletter")
        self.page.check("#optin")
        self.page.fill("#first_name", "John")
        self.page.fill("#last_name", "Tester")
        self.page.fill("#company", "QA Automation")
        self.page.fill("#address1", "123 Testing Street")
        self.page.fill("#address2", "Suite 456")
        self.page.select_option("#country", "United States")
        self.page.fill("#state", "California")
        self.page.fill("#city", "Los Angeles")
        self.page.fill("#zipcode", "90001")
        self.page.fill("#mobile_number", "1234567890")
        self.page.click("button[data-qa='create-account']")
        self.page.wait_for_selector("text=ACCOUNT CREATED!")
        self.page.locator("[data-qa='continue-button']").click()


        for index in range (self.page.locator(".cart_menu td").count()):
            if self.page.locator(".cart_menu td").nth(index).filter(has_text = "total").count()>0:
                colvalue = index
                break

        fancyderss = self.page.locator("tr").filter(has_text = "Women > Tops")
        expect(fancyderss.locator("td").nth(colvalue)).to_have_text("700")






















