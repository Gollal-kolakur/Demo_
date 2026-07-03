from pages.create_account_page import create_account
from pages.sign_up_page import Signup
import json

with open("testdata/login_cred_data.json") as f:
    test_data = json.load(f)
    cred = test_data["user_cred_2"][0]





def test_account_details(browser_page):
    signup = Signup(browser_page)
    signup.open_signup_form()
    name = cred["Name"]
    email = cred["Email"]
    signup.enter_basic_signup_info(name, email)
    account_details = create_account(browser_page)
    account_details.create_account_details()


















