# Generated by Selenium IDE
import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test080802(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    def test_080802(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.set_window_size(1037, 829)
        # self.driver.find_element(By.ID, "kw").send_keys("青春环游记")
        # self.driver.find_element(By.ID, "su").click()
        # time.sleep(6)
        # self.driver.find_element_by_name("wd").clear()
        # time.sleep(3)
        # self.driver.find_element_by_name("wd").send_keys("I love u")
        # self.driver.find_element_by_name("wd").submit()
        # test = self.driver.find_element_by_id("s-bottom-layer-right").text
        title = self.driver.title
        print(title)
        # print("text="+test)
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
