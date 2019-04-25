import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class SeleniumTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = self.get_web_driver()

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def get_web_driver():
        options = Options()
        if os.environ.get('HEADLESS_MODE', False):
            options.add_argument('--headless')
        return webdriver.Chrome(executable_path='./chromedriver', options=options)