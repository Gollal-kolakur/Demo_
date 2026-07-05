

from playwright.sync_api import expect

from pages.sign_up_page import  Signup


import json


from utils.logger import get_logger
logger = get_logger(__name__)


with open("testdata/login_cred_data.json") as f:
    test_data = json.load(f)
    user_cred = test_data["user_credentials"][0]
    user_cred2 = test_data["user_cred_2"][1]





def test_signup_wrong_cred(browser_page):
    signup = Signup(browser_page)
    signup.open_signup_form()
    name =user_cred["username"]
    email =user_cred["password"]
    signup.basic_signup_wrong(name, email)
    msg = signup.error_pop_up()
    print("Validation message:", msg)
    assert "@" in msg

def test_existing_email(browser_page):
    signup = Signup(browser_page)
    signup.open_signup_form()
    name = user_cred2["Name"]
    email = user_cred2["Email"]
    signup.enter_basic_signup_info(name, email)
    prompt = browser_page.get_by_text("Email Address already exist!")
    expect(prompt).to_be_visible()
    expect(prompt).to_have_text("Email Address already exist!")



































































