from playwright.sync_api import Playwright, Page
import pytest

def pytest_addoption(parser):
    group = parser.getgroup("browser")
    group.addoption(
        "--browsername",
        action="store",
        dest="browser_n",
        default="chromium",
        help="Browser: chromium, firefox, webkit"
    )


@pytest.fixture
def browser_page(playwright, request ): #p is an instance object to control the browser engine
    browser_name = request.config.getoption("browser_n")
    print("BROWSER VALUE:", request.config.getoption("browser_n"))
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True,slow_mo=1000)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True, slow_mo=1000)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=True, slow_mo=1000)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context= browser.new_context()
    pg = context.new_page()
    yield pg
    pg.close()
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def home_page(browser_page:Page):
        browser_page.goto("https://automationexercise.com/", wait_until="domcontentloaded")
        yield browser_page


























