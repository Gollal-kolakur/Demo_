from playwright.sync_api import Playwright, expect

from conftest import browser_page


class Signup:
    """
        Page Object Model for the Signup page of Automation Exercise.
        Handles navigation, opening signup form, and entering basic signup info.

    """
    #Locator
    sign_up_link = "Signup / Login" #text
    header_name = "New User Signup!" #text
    name_box = 'input[type="text"]'   #tag with attribute
    email_box = "//input[@data-qa='signup-email']"   # relative xpath
    sign_up_button = "//button[@data-qa='signup-button']" # relative xpath
    create_account_header = "Enter Account Information" # text

    def __init__(self,page):
        self.page = page


    def open_signup_form(self,email,name):
        self.page.get_by_role("link", name= self.sign_up_link).click()
        validation = self.page.get_by_role("heading", name = self.header_name)
        expect(validation).to_be_visible()
        self.page.locator(self.name_box).fill(email)
        self.page.locator(self.email_box).fill(name)   # relative xpath //tag[attribute] will find all from input
        self.page.locator(self.sign_up_button).click()
        account_page_header = self.page.get_by_role("heading", name= self.create_account_header)
        expect(account_page_header).to_be_visible()






















