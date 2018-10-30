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
    '''配置文件、登录用户名、密码'''
    cfgfile = os.path.abspath('.') + '/config.ini'
    url = excuteCFG.ConfigRead(cfgfile, 'setting', 'CPK_URL').CfgRead()
    username = excuteCFG.ConfigRead(cfgfile, 'setting', 'USERNAME').CfgRead()
    password = excuteCFG.ConfigRead(cfgfile, 'setting', 'PASSWORD').CfgRead()
    waittime = excuteCFG.ConfigRead(cfgfile, 'setting', 'WAITTIME').CfgRead()

except IOError, e:
    # pass
    baseinfo.getErrorInfo('获取配置文件异常')


class Login(unittest.TestCase):

    def setUp(self):
        print cfgfile
        print url
        print waittime
        print type(waittime)
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(waittime)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        # self.driver.get('192.168.100.4:10028')
        # print self.driver.current_url()
        self.driver.get(url)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/input[2]').tag_name,
                         'input')

    def test_login_homepage(self):
        print url
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/input[2]').send_keys(username)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/input[2]').send_keys(password)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/button').click()
        self.driver.implicitly_wait(waittime)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/h1').text, u'首页概览')

    def tearDown(self):

        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        '''
        self.driver.find_element_by_xpath('//*[@id="header"]/ul/li[2]/button').click()
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="header"]/ul/li[2]/ul/li[2]/a').click()
        self.driver.implicitly_wait(waittime)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/input[2]').tag_name,
                         'input')
        self.driver.implicitly_wait(waittime)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        '''
if __name__ == "__main__":
    unittest.main()
