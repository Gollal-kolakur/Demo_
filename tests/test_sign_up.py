

from playwright.sync_api import expect

from pages.sign_up_page import  Signup


import json


from utils.logger import get_logger
logger = get_logger(__name__)


with open("testdata/login_cred_data.json") as f:
    test_data = json.load(f)
    user_cred = test_data["user_credentials"][0]



def test_registration(browser_page):
    logger.info(f"launching the browser and page: {browser_page.url}")
    browser_page.pause()
    pass

def test_signup_wrong_cred(browser_page):
    signup = Signup(browser_page)
    signup.open_signup_form()
    name =user_cred["username"]
    email =user_cred["password"]
    signup.basic_signup_wrong(name, email)
    msg = signup.error_pop_up()
    print("Validation message:", msg)
    assert "@" in msg

def test_existing_email(home_page, sign_cred):
    signup = Signup(home_page)
    signup.open_signup_form()
    data = sign_cred["New_signup"]
    name = data["Name"]
    email = data["Email"]
    signup.enter_basic_signup_info(name, email)
    prompt = home_page.get_by_text("Email Address already exist!")
    expect(prompt).to_be_visible()
    expect(prompt).to_have_text("Email Address already exist!")



































































