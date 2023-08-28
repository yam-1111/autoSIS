from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
from autoSIS.scraper import scraper
import re


class autoSIS:
    SIS_WEBSITE = "https://sis1.pup.edu.ph/student/"

    def __init__(
        self,
        # testing state
        student_no : str,
        student_birthday : str,
        student_password : str,
        screenshot_path="screenshot.png",
        uri_destination="grades",
        timeout=50000,
        retry_count = 3,
        isheadless=True,
        isscreenshot=True
    ):

        self.student_no = student_no
        self.student_birthday = student_birthday.split("/")
        self.student_password = student_password
        self.uri_destination = uri_destination
        self.timeout = timeout
        self.retry_count = retry_count
        self.isheadless = isheadless
        self.isscreenshot = isscreenshot
        self.screenshot_path = screenshot_path

        # local assets
        self.html_content = ""
        self.RETRY_COUNT = 0

        # storing the playwright instance
        self.RETRY_COUNT = self.retry_count
        with sync_playwright() as play:
            self.browser = play.firefox.launch(headless=self.isheadless)
            self.page = self.browser.new_page()
            self.page.set_default_timeout(self.timeout)

            self.login()

    def login(self):
        print(f"[DEBUG] logging in : {self.SIS_WEBSITE}\n")
        try:
            self.page.goto(self.SIS_WEBSITE)
        except Exception as error:
            if not self.RETRY_COUNT == 0:
                print(f"{error}\n\n[DEBUG] retrying to do request.. attempt {self.RETRY_COUNT}")
                self.RETRY_COUNT -=1
                self.login()
            print(f"\n{error}")
            self.browser.close()
        try:
            if self.page.query_selector("#studno"):
                self.page.fill("#studno", self.student_no)
                self.page.select_option("#SelectMonth", self.student_birthday[0])
                self.page.select_option("#SelectDay", self.student_birthday[1])
                self.page.select_option("#SelectYear", self.student_birthday[2])
                self.page.fill("#password", self.student_password)
                self.page.click("input[name='Login']")

                URL_DESTINATION = "/".join(self.page.url.rsplit("/", 1)[0:1]) + "/"
                self.page.goto(URL_DESTINATION + self.uri_destination)
                print(f"[DEBUG] Going to : {URL_DESTINATION+self.uri_destination}\n")
                self.html_content = self.page.content()

                if self.isscreenshot:
                    self.screenshot()
                self.browser.close()
        except Exception as error:
            if not self.RETRY_COUNT == 0:
                    print(f"{error}\n\n[DEBUG] retrying to do request.. attempt {self.RETRY_COUNT}")
                    self.RETRY_COUNT -=1
                    self.login()
            print(f"\n{error}")
            self.browser.close()

    def screenshot(self):
        print("[DEBUG] Taking screenshot\n")
        self.page.screenshot(path=self.screenshot_path, full_page=True)
        print(f"[DEBUG] saving to {self.screenshot_path}")
        
    # class functions
    def dump_as_file(self, html_path="index.html"):
        print(f"[DEBUG] exporting the html in {html_path}\n")
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(self.html_content)

    def get_grades(self, raw_text=False, custom_mapping=None):
        try:
            return scraper(self.html_content, custom_mapping=custom_mapping)
        except Exception as error:
            return error

