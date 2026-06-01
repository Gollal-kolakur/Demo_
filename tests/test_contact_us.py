from pages.contact_us import contact_us




def test_contact_us(home_page):
    contact = contact_us(home_page)
    contact.navigate_contact_page()







