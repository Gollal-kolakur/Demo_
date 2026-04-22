from pages.create_account_page import create_account
from pages.Sign_up_page import Signup
import json


with open("testdata/login_cred_data.json") as f:
    test_data = json.load(f)
    credential2 = test_data["sign_up_credentials"]




def test_account_details(browser_page):
    signup = Signup(browser_page)
    data = credential2["tag"]
    name = credential2["name"]
    email = credential2["email"]
    password = credential2["password"]
    signup.open_signup_form(name,email)
    account_details = create_account(browser_page)
    account_details.create_account_details(password)

""""self.page.get_by_role("link", name = "Contact us").click()
       expect(self.page.get_by_text("Get In Touch")).to_be_visible()

       self.page.get_by_placeholder("Name").fill("Gollal")
       self.page.locator("input[data-qa='email']").fill("gollal009@gmail.com")
       subject = self.page.locator("input[data-qa='subject']")
       expect(subject).to_be_visible()
       subject.fill("djbsjdb")

       self.page.locator("#message").fill("djbsjdb")

       self.page.set_input_files("input[type='file']", r"C:\Users\BEQ\Desktop\trial.txt")

       self.page.on("dialog",lambda dialog:dialog.accept())
       self.page.get_by_role("button", name = "Submit").click()
       self.page.wait_for_timeout(10000)

       success = self.page.locator(".status.alert-success")
       expect(success).to_be_visible(timeout=10000)

       self.page.locator(".btn-success").click()"""
















