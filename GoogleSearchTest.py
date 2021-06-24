from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import unittest


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_search_automationstepbystep(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()


    def test_search_automations(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Automation in python")
        self.driver.find_element_by_name("btnK").click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        cls.print("test completed")



