from pages.search import search_page
from playwright.sync_api import Playwright





def test_search(browser_page):
    search_item = search_page(browser_page)
    print(search_item)
    search_item.search_product()


def test_API(playwright:Playwright):
    api_request_context = playwright.request.new_context(base_url = "https://automationexercise.com/api/productsList")
    response = api_request_context.get("/")







