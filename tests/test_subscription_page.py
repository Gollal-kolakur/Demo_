from playwright.sync_api import Page
from pages.subscription_page import SubscriptionPage
    
    
    
def test_subscribe(browser_page):
    sub = SubscriptionPage(browser_page)
    sub.subscription()


