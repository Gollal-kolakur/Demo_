from playwright.sync_api import expect




class LogInPage:


    sign_up_link = "Signup / Login"
    header_name = "New User Signup!"
    Log_in_header = "Login to your account"
    email_box = "input[data-qa='login-email']"
    password_box = "input[data-qa='login-password']"
    Log_in_button = "button[data-qa='login-button']"
    error_message = "p:has-text('Your email or password is incorrect!')" # tag with text
    error_ppop_up_username = "document.querySelector('input[data-qa=login-email]').validationMessage" # pop-up from web html not app can use to see .checkValidity()
    error_pop_up_password = "document.querySelector('input[data-qa=login-password]').validationMessage"
    log_in_icon = "i.fa.fa-user"
    logout_link_name = "logout"

    def __init__(self ,page):
        self.page = page

    def login_button_click(self,email, password):              #  email, password
        self.page.get_by_role("link", name=self.sign_up_link).click()
        self.page.get_by_role("heading", name=self.header_name)
        header = self.page.get_by_text(self.Log_in_header)
        expect(header).to_be_visible()
        self.page.locator(self.email_box).fill(email)
        self.page.locator(self.password_box).fill(password)
        self.page.locator(self.Log_in_button).click()

    def valid_log_in(self):
        validation = self.page.get_by_text("Logged in")
        expect(validation).to_be_visible()

    def invalid_log_in(self):
        validation = self.page.locator(self.error_message)
        expect(validation).to_be_visible()

    def invalid_user_name(self):
        pop_up = self.page.evaluate(self.error_ppop_up_username)
        print(pop_up)
        assert pop_up != ""  #
        assert "@" in pop_up  # assert is used to check the condition is passing or failing

    def invalid_password(self):
        pop_up = self.page.evaluate(self.error_pop_up_password)
        print(pop_up)
        assert pop_up != ""  #
        assert "Please fill out this field" in pop_up  # assert is used to check the condition is passing or failing

    def log_out(self,email, password):
        self.login_button_click(email, password)
        logged_in_icon = self.page.locator(self.log_in_icon)
        expect(logged_in_icon).to_be_visible()
        log_out_link = self.page.get_by_role("link", name= self.logout_link_name)
        log_out_link.click()
        expect(logged_in_icon).to_be_hidden()
        expect(log_out_link).to_be_hidden()




