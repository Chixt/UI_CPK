#!/usr/bin/env python
# encoding:utf-8
import sys

sys.path.append('./venv/lib/python2.7/site-packages')
import unittest
from selenium import webdriver
import os
from base import excuteCFG
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base import baseinfo

try:
    cfgfile = os.path.abspath('.') + '/config.ini'  # 配置文件位置
    url = excuteCFG.ConfigRead(cfgfile, 'setting', 'CPK_URL').CfgRead()
    username = excuteCFG.ConfigRead(cfgfile, 'setting', 'USERNAME').CfgRead()
    password = excuteCFG.ConfigRead(cfgfile, 'setting', 'PASSWORD').CfgRead()
    waittime = excuteCFG.ConfigRead(cfgfile, 'setting', 'WAITTIME').CfgRead()
except IOError, e:
    baseinfo.getErrorInfo('获取配置文件异常')


class Logout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(waittime)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(url)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/input[2]').tag_name,
                         'input')
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/input[2]').send_keys(username)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/input[2]').send_keys(password)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/button').click()
        self.driver.implicitly_wait(waittime)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/h1').text, u'首页概览')
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='pull-right close']")))
        self.driver.find_element_by_xpath("//button[@class='pull-right close']").click()
        self.driver.implicitly_wait(waittime)

    def test_logout(self):
        self.driver.find_element_by_xpath('//*[@id="header"]/ul/li[2]/button').click()
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="header"]/ul/li[2]/ul/li[2]/a').click()
        self.driver.implicitly_wait(waittime)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/input[2]').tag_name,
                         'input')
        self.driver.implicitly_wait(waittime)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


'''
if __name__ == "__main__":
    unittest.main()
'''
