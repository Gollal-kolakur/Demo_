from pages.Sign_up_page import Signup
from pages.Log_in import LogInPage
import json
import pytest

with open("testdata/login_cred_data.json") as f:
    test_data = json.load(f)
    credential1 = test_data["user_credentials"]
    credential_1 = test_data["user_credentials"] [0]


@pytest.mark.parametrize("user_cred",credential1)
def test_login(browser_page,user_cred):
    data = user_cred["tag"]
    email = user_cred["username"]
    password = user_cred["password"]
    login = LogInPage(browser_page)
    login.login_button_click(email, password)

    if data == "valid":
        login.valid_log_in()
    elif data == "invalid":
        login.invalid_log_in()
    elif data == "invalid_user":
        login.invalid_user_name()
    elif data == "invalid_password":
        login.invalid_password()
    else:
        print("empty test data")

def test_logout(browser_page):
    logout=LogInPage(browser_page)
    email = credential_1["username"]
    password = credential_1["password"]
    logout.log_out(email,password)


















