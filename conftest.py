from playwright.sync_api import Playwright
import pytest
from pathlib import Path
from dotenv import load_dotenv
import os

def pytest_addoption(parser):
    group = parser.getgroup("browser")
    group.addoption(
        "--browsername",
        action="store",
        dest="browser_n",
        default="chromium",
        help="Browser: chromium, firefox, webkit"
    )
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        choices=["qa", "staging"],
        help="Environments to run tests: qa or staging"
    )


@pytest.fixture(scope="session", autouse=True)
def load_env(request):

    if os.environ.get("base_url"):
        return
    env_name = request.config.getoption("--env")
    env_file = Path(__file__).parent / f".env.{env_name}"

    if env_file.exists():
        load_dotenv(dotenv_path=env_file)
    else:
        pytest.exit(f"Error: {env_file.name} No such file")


@pytest.fixture(scope = "function")
def browser_page(playwright:Playwright, request ): #p is an instance object to control the browser engine
    browser_name = request.config.getoption("browser_n")

    url = os.environ.get("base_url")

    if not url:
        raise ValueError("Error: In .env file No base_url !")

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





























