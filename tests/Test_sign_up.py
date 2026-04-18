

from playwright.sync_api import expect

from pages.Sign_up_page import  Signup





from utils.logger import get_logger
logger = get_logger(__name__)





def test_registration(browser_page):
    logger.info(f"launching the browser and page: {browser_page.url}")
    browser_page.pause()
    pass

def test_signup_wrong_cred(home_page, sign_cred):
    signup = Signup(home_page)
    signup.open_signup_form()
    data = sign_cred["wrong_signup"]
    name =data["Name"]
    email =data["Email"]
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


































































