from pages.contact_us import contact_us


def test_contact_us(browser_page):
    context = browser_page.context
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    try:
        contact = contact_us(browser_page)
        contact.navigate_contact_page()
    finally:

        context.tracing.stop(path="my_trace.zip")








