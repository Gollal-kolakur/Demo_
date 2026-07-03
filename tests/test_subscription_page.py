from playwright.sync_api import Page
from pages.subscription_page import subscription_page
    
    
    
def test_subscribe(browser_page):
    sub = subscription_page(browser_page)
    sub.subscription()


