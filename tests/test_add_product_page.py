from playwright.sync_api import Page
from pages.add_product_page import add_product_cart

def test_add_product_details(page2:Page, home_page):
    product = add_product_cart(page2)
    product.add_product()


