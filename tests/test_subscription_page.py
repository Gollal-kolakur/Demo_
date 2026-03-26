from playwright.sync_api import Page
from pages.Subscription_page import subscription_page
    
    
    
def test_subscribe(home_page):
    sub = subscription_page(home_page)
    sub.subscription()


