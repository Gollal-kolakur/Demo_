from playwright.sync_api import Page
from pages.add_product_page import add_product_cart

def test_add_product_details(browser_page):
    product = add_product_cart(browser_page)
    product.add_product()

def test_flipkart(page:Page):
    page.goto("https://www.flipkart.com/")
    page.get_by_role("textbox", name = "Search for Products, Brands and More").fill("Mobile")