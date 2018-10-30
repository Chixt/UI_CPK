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
    '''导航窗口，首页'''
    homepage = excuteCFG.ConfigRead(cfgfile, 'dashboard', 'homepage').CfgRead()
    '''应用安装卸载升级评分分析日历'''
    calendar = excuteCFG.ConfigRead(cfgfile, 'homepage', 'calendar').CfgRead()
    calendar_option = excuteCFG.ConfigRead(cfgfile, 'homepage', 'calendar').CfgRead()
    calendar_day = excuteCFG.ConfigRead(cfgfile, 'homepage', 'calendar_day').CfgRead()
    calendar_week = excuteCFG.ConfigRead(cfgfile, 'homepage', 'calendar_week').CfgRead()
    calendar_month = excuteCFG.ConfigRead(cfgfile, 'homepage', 'calendar_month').CfgRead()
    calendar_year = excuteCFG.ConfigRead(cfgfile, 'homepage', 'calendar_year').CfgRead()

except IOError, e:
    baseinfo.getErrorInfo()


class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(waittime)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/input[2]').send_keys(username)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/input[2]').send_keys(password)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/button').click()
        self.driver.implicitly_wait(waittime)
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='pull-right close']")))
        self.driver.find_element_by_xpath("//button[@class='pull-right close']").click()
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/h1').text, u'首页概览')

    def test_calendar(self):

        # 应用安装卸载升级评分分析
        for i in range(1, 4):
            self.driver.implicitly_wait(waittime)
            self.assertTrue(self.driver.find_element_by_xpath(calendar_day))
            self.assertTrue(self.driver.find_element_by_xpath(calendar_week))
            self.assertTrue(self.driver.find_element_by_xpath(calendar_month))
            self.assertTrue(self.driver.find_element_by_xpath(calendar_year))
            self.driver.find_element_by_xpath(calendar_option.replace('li[i]', 'li[%d]' % i)).click()
            self.driver.find_element_by_xpath(calendar).click()
        self.driver.find_element_by_xpath(homepage).click()

    def tearDown(self):
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        '''

if __name__ == "__main__":
    unittest.main()
