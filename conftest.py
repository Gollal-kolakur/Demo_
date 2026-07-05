from playwright.sync_api import Playwright, Page
import pytest

def pytest_addoption(parser):
    group = parser.getgroup("browser")
    group.addoption(
        "--browsername", action="store", dest="browser_n", default="chromium", help="Browser: chromium, firefox, webkit"
    )

    group.addoption(
        "--url", action="store", dest="url_links", default="https://automationexercise.com/"
    )


@pytest.fixture(scope = "function")
def browser_page(playwright, request ): #p is an instance object to control the browser engine
    browser_name = request.config.getoption("browser_n")
    url = request.config.getoption("url_links")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True,slow_mo=2000)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True,slow_mo=2000)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=True,slow_mo=2000)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context= browser.new_context()
    pg = context.new_page()
    pg.goto(url)
    yield pg
    pg.close()
    context.close()
    browser.close()

def test_tril(browser_page):
    pass



























