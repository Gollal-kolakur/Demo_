from playwright.sync_api import expect


class add_product_cart():





    def __init__(self,page):
        self.page = page


    def add_product(self):
        self.page.get_by_role("link", name="products").click()
        item = self.page.get_by_role("heading", name="All Products")
        expect(item).to_be_visible()
        first_product = self.page.locator(".product-image-wrapper").nth(0)
        first_product.hover()
        first_product.locator(".add-to-cart").nth(0).click()
        self.page.get_by_role("button", name ="Continue Shopping").click()
        second_product = self.page.locator(".product-image-wrapper").nth(1)
        second_product.hover()
        second_product.locator(".add-to-cart").nth(1).click()
        self.page.get_by_role("button", name="Continue Shopping").click()