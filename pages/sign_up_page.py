from playwright.sync_api import Playwright, expect




class Signup:
    """
        Page Object Model for the Signup page of Automation Exercise.
        Handles navigation, opening signup form, and entering basic signup info.

    """
    #Locator

    HOME_TEXT = "Home"
    SIGN_UP_TEXT = "New User Signup!"
    CREATE_ACCOUNT_TEXT = "Enter Account Information"




    def __init__(self,page):
        self.page = page




    def open_signup_form(self):
        self.page.get_by_role("link", name = "Signup/Login").click()
        self.page.pause()
        sign_up = self.page.get_by_text(self.SIGN_UP_TEXT)



    def enter_basic_signup_info(self, name, email):
        self.page.locator("input[name='name']").fill(name)
        self.page.locator("input[data-qa='signup-email']").fill(email)
        self.page.get_by_role("button", name="Signup").click()
        self.page.wait_for_load_state("load")


    def basic_signup_wrong(self, name, email):
        self.page.locator("input[name='name']").fill(name)
        self.page.locator("input[data-qa='signup-email']").fill(email)
        self.page.get_by_role("button", name="Signup").click()


    def error_pop_up(self):
        email = self.page.wait_for_selector('input[data-qa="signup-email"]')
        validation_msg = email.evaluate("el => el.validationMessage")
        return validation_msg



















