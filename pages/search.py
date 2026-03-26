from playwright.sync_api import expect


class search_page():

    def __init__(self,page):
        self.page = page


    def search_product(self):
        self.page.get_by_role("link", name = "Products").click()
        self.page.locator("#search_product").fill("Men Tshirt")
        self.page.locator("#submit_search").click()
        expect(self.page.get_by_role("heading", name="Searched Products")).to_be_visible()
        products = self.page.locator(".productinfo p")
        count = products.count()
        print("Total products found:", count)

        for i in range(count):
            text = products.nth(i).text_content()
            print(text)
        assert "Tshirt" in text


