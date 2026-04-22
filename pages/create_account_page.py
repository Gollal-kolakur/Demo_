

from playwright.sync_api import Playwright, expect
from pages.Sign_up_page import Signup





class create_account:

    title = "#id_gender1"
    name = "input[data-qa='name']"
    email = "#email"
    password_box = "#password"
    news_letter_check = "label[for='newsletter']"
    offer_letter_check = "label[for='optin']"


    def __init__(self ,page):
        self.page = page
        print(self.page)

    def create_account_details(self,password):
        #Enter account information
        self.page.wait_for_load_state("load")
        self.page.locator(self.title).check()
        validation_name = self.page.locator(self.name)
        assert validation_name != ""
        expect(self.page.locator(self.email)).not_to_have_value("")
        self.page.locator(self.password_box).fill(password)
        self.page.select_option("#days", "10")                     # select_option to select from dropdown
        self.page.select_option("#months", "5")
        self.page.select_option("#years", "1995")
        self.page.locator(self.news_letter_check).check()
        self.page.locator(self.offer_letter_check).check()


        #Adress Information
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
        self.page.get_by_role("link", name= "Delete Account").click()
        self.page.locator("a[data-qa='continue-button']").click()
        print("account created and deleted successfully")



















