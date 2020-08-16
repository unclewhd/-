import unittest
import time
from selenium import webdriver
class Test2(unittest.TestCase):
    def test2(self):

        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        time.sleep(2)
        url = driver.current_url
        print(url)
        time.sleep(1)