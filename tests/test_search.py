from pages.search import search_page



def test_search(browser_page):
    search_item = search_page(browser_page)
    search_item.search_product()





