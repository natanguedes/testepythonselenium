# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#codigo exportado do plugin katalon recorder
class Test1(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome("D:\\testes\\chromedriver\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):

        self.driver.get("http://www.google.com/")

        # Abre uma nova aba
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

        # Carrega a nova aba
        self.driver.get('http://stackoverflow.com/')

        self.driver.get("http://www.python.org")
        self.assertIn("Python", self.driver.title)
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Python", self.driver.title)
        print(self.driver.title)
        # Fecha a aba
      #@  self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

        # self.driver.close()
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
