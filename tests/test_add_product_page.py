from playwright.sync_api import Page
from pages.add_product_page import add_product_cart

def test_add_product_details(browser_page):
    product = add_product_cart(browser_page)
    product.add_product()


def test_amazon(page:Page):
    page.goto("https://www.amazon.in/?tag=msndeskabkin-21&ref=pd_sl_5twasf2d2w_e&adgrpid=1318316051640309&hvadid=82395086169651&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=116072&hvtargid=kwd-82395637438085%3Aloc-90&hydadcr=5652_2501626&mcid=b983ec7c37413e6ab8b5124ff4bfc77b&language=en_IN")
    page.get_by_role("link", name = "हिन्दी").click()



