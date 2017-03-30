# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# python 2.7.10
# selenium 2.53.1


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.161:8081/CardPlatform"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_yumb2b(self):
        driver = self.driver
        # 登录
        driver.get(self.base_url + "/login.jsp")
        driver.find_element_by_id("user_id").clear()
        driver.find_element_by_id("user_id").send_keys("aaaa")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("000000")
        driver.find_element_by_xpath("//img[contains(@onclick,'login2();')]").click()

        return 

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
