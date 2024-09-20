import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ExampleFunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()

    def test_heading_text_is_correct(self):
        # Go to the login page
        self.browser.get("http://localhost:8000/login/")
        
        # Find the login form fields and log in as a test user
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("test")  # Replace with the actual test username
        password_input.send_keys("usertest")  # Replace with the actual test password
        
        # Locate the submit button and click it (using class name here)
        login_button = self.browser.find_element(By.CLASS_NAME, "login_btn")
        login_button.click()
        
        # Now go to the homepage
        self.browser.get("http://localhost:8000")
        
        # Verify the heading text is correct
        element: WebElement = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Mental Health Tracker", element.text)
    
    def test_page_title_is_correct(self):
        self.browser.get("http://localhost:8000")

        self.assertEqual("PBD Mental Health Tracker", self.browser.title)
