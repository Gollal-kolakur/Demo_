import pytest
from playwright.sync_api import Playwright, Page , expect
import json
from pathlib import Path


@pytest.fixture(scope="function")
def page2(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()




@pytest.fixture(scope="function")
def sign_cred():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir/"Test_data"/"credential.json"
    with open(file_path) as f:
        test_data = json.load(f)
        user_cred = test_data['User_credential']
        return user_cred


@pytest.fixture(scope="function")
def home_page(page2:Page):
    page2.goto("https://automationexercise.com/", wait_until="domcontentloaded")
    return page2






