from playwright.sync_api import Page
from pages.subscription_page import subscription_page
    
    
    
def test_subscribe(home_page):
    sub = subscription_page(home_page)
    sub.subscription()


