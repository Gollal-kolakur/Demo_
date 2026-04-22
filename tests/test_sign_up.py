from pages.Sign_up_page import  Signup
import json
import pytest


with open("testdata/login_cred_data.json") as f:
    test_data = json.load(f)
    credential1 = test_data["user_credentials"]
    credential2 = test_data["sign_up_credentials"]




def test_sign_up(browser_page):
    sign = Signup(browser_page)
    name = credential2["name"]
    email = credential2["email"]
    sign.open_signup_form(name,email)




































































