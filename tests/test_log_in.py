from pages.sign_up_page import Signup
from pages.log_in import LogInPage




def test_login(home_page, sign_cred):
    signup = Signup(home_page)
    signup.open_signup_form()
    data = sign_cred["valid_login"]
    email = data["email"]
    password = data["password"]
    lgin = LogInPage(home_page)
    lgin.login(email, password)

def test_wrong_login(home_page, sign_cred):
    signup = Signup(home_page)
    signup.open_signup_form()
    data = sign_cred["wrong_login"]
    email = data["email"]
    password = data["password"]
    login = LogInPage(home_page)
    login.wrong_login(email, password)










