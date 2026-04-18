from pages.search import search_page





def test_search(home_page):
    search_item = search_page(home_page)

    print(search_item)
    search_item.search_product()





