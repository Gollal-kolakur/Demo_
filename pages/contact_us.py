from playwright.sync_api import expect
from playwright.sync_api import Page, expect
from pathlib import Path

class contact_us:

    def __init__(self, page):
        self.page = page


    def navigate_contact_page(self,name,email):
       self.page.locator("i.fa.fa-envelope").click()
       header = self.page.get_by_role("heading", name= "Feedback For Us")
       expect(header).to_be_visible()
       self.page.get_by_placeholder("Name").fill(name)
       self.page.locator("input[data-qa='email']").fill(email)
       self.page.get_by_placeholder("Subject").fill("fbsudvja")
       self.page.locator("//textarea[@data-qa='message']").fill("fsodckds")
       file_path = Path(__file__).parent.parent / "testdata" / "interview_coding_question.txt"
       print(file_path)
       self.page.locator("input[name='upload_file']").set_input_files(file_path)
       self.page.locator("input[data-qa='submit-button']").click()
       self.page.on("dialog", lambda dialog:dialog.accept())
       self.page.get_by_role("link", name= "Home").click()
       home_page_header = self.page.get_by_role("heading", name= "Features Items")
       expect(home_page_header).to_be_visible()





























