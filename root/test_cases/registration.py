import time

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from root.utils import Utils


class Registration():
    def __init__(self):
        """This will assign config data and registration page locators as class variable"""
        self.config=Utils()
        self.page_locators=Utils().get_page_locators(self.__class__.__name__.lower())
        self.user_data=self.config.load_excel_data()
        
    def get_element(self,element_name):
        """This method will return Key and Value of page element from class attribute"""
        locator_info=self.page_locators[element_name]
        return getattr(By,locator_info['by'].upper()),locator_info['value']

    
    def test_register_new_user(self,user_id, browser_name=None):
        user_data=self.user_data[int(user_id)-1]
        # print(type(user_id))
        # print(type(int(user_id)))
        driver=self.config.launch_browser(self.config.base_url,browser_name)
        assert True if driver.title == "ParaBank | Welcome | Online Banking" else print(AssertionError("Home Page Not Found"))
        driver.find_element(*self.get_element('register_link')).click()
        assert True if driver.title =="ParaBank | Register for Free Online Account Access" else print(AssertionError("Register Page Not Found"))
        driver.find_element(*self.get_element('first_name')).send_keys(user_data['First_Name'].strip())
        driver.find_element(*self.get_element('last_name')).send_keys(user_data['Last_Name'].strip())
        driver.find_element(*self.get_element('address')).send_keys(user_data['Address'].strip())
        driver.find_element(*self.get_element('city')).send_keys(user_data['City'].strip())
        driver.find_element(*self.get_element('state')).send_keys(user_data['State'].strip().strip())
        driver.find_element(*self.get_element('zip_code')).send_keys(user_data['Zip_Code'])
        driver.find_element(*self.get_element('phone')).send_keys(user_data['Phone'])
        driver.find_element(*self.get_element('ssn_number')).send_keys(user_data['SSN_Number'])
        username_string=self.config.get_random_strin(3)
        driver.find_element(*self.get_element('user_name')).send_keys(user_data['Username'].strip()+username_string)
        driver.find_element(*self.get_element('password')).send_keys(user_data['Password'].strip())
        driver.find_element(*self.get_element('repeate_password')).send_keys(user_data['Confirm'].strip())
        driver.find_element(*self.get_element('register_button')).click()
        user_creation=driver.find_element(*self.get_element('user_create'))
        time.sleep(1)
        WebDriverWait(driver,2).until(EC.visibility_of(user_creation))
        assert True if driver.title =="ParaBank | Customer Created" else print(AssertionError("Customer Creation Page Not Found"))
        assert True if user_creation.text == f"Welcome {user_data['Username'].strip()+username_string}" else print(AssertionError(f"User {user_data['Username'].strip()} Not Created"))
        driver.find_element(*self.get_element('logout_link')).click()
        home_page=driver.find_element(*self.get_element('customer_login'))
        WebDriverWait(driver,2).until(EC.visibility_of(home_page))
        assert True if driver.title == "ParaBank | Welcome | Online Banking" else print(AssertionError("Home Page Not Found"))
        driver.close()
    
        
# reg=Registration()
# reg.test_register_new_user("1")