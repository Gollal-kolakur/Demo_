from playwright.sync_api import expect




class LogInPage:


    def __init__(self ,page):
        self.page = page

    def login_button(self,email,password):
        self.page.locator("i[class='fa fa-lock']").click()
        assertion = self.page.get_by_role("heading", name = "Login to your account")
        expect(assertion).to_be_visible()
        self.page.locator("input[data-qa='login-email']").fill(email)
        self.page.locator("input[data-qa = 'login-password']").fill(password)
        self.page.locator("//button[@data-qa='login-button']").click()

    def valid_login(self,email,password):
        pass

    def invalid_login(self):
        assertion = self.page.locator("p:has-text('Your email or password is incorrect!')")
        expect(assertion).to_be_visible()

    def invalid_user(self):
        validation_msg = self.page.eval_on_selector(
            "input[data-qa='login-email']",
            "el => el.validationMessage"
        )
        assert validation_msg != ""
        assert "@" in validation_msg



    def invalid_password(self):
        validation_msg = self.page.eval_on_selector(
            "input[data-qa='login-password']",
            "el => el.validationMessage")

        is_valid = self.page.eval_on_selector(
            "input[data-qa='login-password']",
            "el => el.validity.valid"
        )

        print(f"Message: '{validation_msg}'")
        print(f"Tooltip visible: {not is_valid}")

        assert validation_msg != ""
        assert "Please fill out this field" in validation_msg











