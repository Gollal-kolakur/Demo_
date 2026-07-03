from pages.contact_us import contact_us




def test_contact_us(browser_page):
    contact = contact_us(browser_page)
    contact.navigate_contact_page()







