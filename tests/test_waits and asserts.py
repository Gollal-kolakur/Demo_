# Types of waits and asserts in python
"""In Playwright, waits and assertions are much smarter and cleaner
compared to Selenium. You don’t manually handle waits much because
Playwright has auto-waiting built in"""

#Types of wait in playwright
"""Playwright automatically waits for: No need of putting wait methods generally
Element to be visible
Element to be enabled
Element to be stable"""

#other waits
#Wait for selector
"""wait_for_selector() ex:page.wait_for_selector("#login")"""

#wait for page load
"""page.wait_for_load_state("load")        # full load
page.wait_for_load_state("domcontentloaded")
page.wait_for_load_state("networkidle")""" #most used

#wait for url
"""page.wait_for_url("**/dashboard")"""

#Locator based(most used)
"""locator = page.locator("#login")
locator.wait_for(state="visible")"""

#Types of Assertions in Playwright

#Visibility Assertions - commonly used
"""from playwright.sync_api import expect
expect(page.locator("#login")).to_be_visible()
expect(page.locator("#login")).to_be_hidden()"""

#Text assertion - commonly used
"""expect(page.locator("h1")).to_have_text("Welcome")
expect(page.locator("h1")).to_contain_text("Welcome")"""

#atrribute assertaion
"""expect(page.locator("#input")).to_have_attribute("type", "text")
expect(page).to_have_url("https://example.com/dashboard") # commonly used
expect(page).to_have_title("Dashboard")
expect(page.locator(".item")).to_have_count(5)"""