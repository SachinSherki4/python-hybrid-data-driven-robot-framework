from pathlib import Path
import time

from selenium.webdriver.common.by import By

from root.utils import Utils

class LoginPage():
    def __init__(self):
        self.config=Utils()
        self.page_locators=Utils().get_page_locators(self.__class__.__name__.lower())
        self.user_data=Utils().load_excel_data()
        
    def get_element(self,element_name):
        """This method will return Key and Value of page element from class attribute"""
        locator_info=self.page_locators[element_name]
        return getattr(By,locator_info['by'].upper()),locator_info['value']
    
    def login_existing_user(self):
        user_data=self.user_data[2]
        driver=self.config.launch_browser(self.config.base_url)
        assert True if driver.title == "ParaBank | Welcome | Online Banking" else print(AssertionError("Home Page Not Found"))
        driver.find_element(*self.get_element('username')).send_keys(user_data['Username'])
        driver.find_element(*self.get_element('password')).send_keys(user_data['Password'])
        driver.find_element(*self.get_element('login_button')).click()
        # text=driver.find_element(*self.get_element('login_verification')).text
        # print(text)
        time.sleep(2)
        assert driver.title == "ParaBank | Accounts Overview", AssertionError("User Not Login")

h=LoginPage()
h.login_existing_user()