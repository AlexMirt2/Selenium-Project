import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

class FacebookLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_facebook_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        print ("Opened facebook")
        sleep(3)
        # Enter username and password
        email_input = driver.find_element(By.ID, "email").send_keys("your_email@example.com")
        print ("Email Id entered")
        password_input = driver.find_element(By.ID, "pass").send_keys("your_password")
        print ("Password entered")

        # Click on the login button
        login_button = driver.find_element(By.NAME, "login").click()

        # Add a delay to allow the page to load after logging in
        sleep(3)

        # Check if login was successful by verifying the presence of the logout button
        logout_button = driver.find_element(By.XPATH, "//div[@aria-label='Account']")
        self.assertTrue(logout_button.is_displayed())
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
