from playwright.sync_api import expect




class LogInPage:


    def __init__(self ,pag):
        self.pa = pag

    def login(self, email, password):
        confirm = self.pa.get_by_text("Login to your account")
        expect(confirm).to_be_visible()
        self.pa.locator("input[data-qa='login-email']").fill(email)
        self.pa.locator("input[data-qa='login-password']").fill(password)
        with self.pa.expect_navigation():
            self.pa.locator("button[data-qa='login-button']").click()
        conf = self.pa.locator(".fa.fa-user")
        expect(conf).to_be_visible()
        delete = self.pa.get_by_role("link", name = "Delete Account")
        expect(delete).to_be_visible()
        delete.click()

    def wrong_login(self, email, password):
        self.pa.locator("input[data-qa='login-email']").fill(email)
        self.pa.locator("input[data-qa='login-password']").fill(password)
        self.pa.locator("button[data-qa='login-button']").click()
        error = self.pa.locator("text=Your email or password is incorrect!")
        error.wait_for(state="visible")



