from pages.create_account_page import create_account
from pages.sign_up_page import Signup







def test_account_details(home_page, sign_cred):
    signup = Signup(home_page)
    signup.open_signup_form()
    data = sign_cred["New_signup"]
    name = data["Name"]
    email = data["Email"]
    signup.enter_basic_signup_info(name, email)
    account_details = create_account(home_page)
    account_details.create_account_details()


















