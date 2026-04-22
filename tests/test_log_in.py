from pages.sign_up_page import Signup
from pages.log_in import LogInPage
import json
import pytest



with open("testdata/login_cred_data.json") as f:
    test_data = json.load(f)
    user_cred_login = test_data["user_credentials"]

@pytest.mark.parametrize("user_cred",user_cred_login)
def test_login(browser_page,user_cred):
    button = LogInPage(browser_page)
    data = user_cred["tag"]
    email = user_cred["username"]
    password = user_cred["password"]
    button.login_button(email,password)

    if data == "valid":
        pytest.skip("not working cred")
    elif data == "invalid":
        button.invalid_login()
    elif data == "invalid_user":
        button.invalid_user()
    elif data == "invalid_password":
        button.invalid_password()
    else:
        print("test data not available")














