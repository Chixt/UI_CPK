#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:ChiXiaotong
@file:test_case51.py
@project:UI_CPK
@software:PyCharm
@time:2018/10/19 下午3:19
"""



import unittest
from base import excuteCFG, baseinfo
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

try:
    url = excuteCFG.GetConfig().getSetting('CPK_URL')
    username = excuteCFG.GetConfig().getSetting('USERNAME')
    password = excuteCFG.GetConfig().getSetting('PASSWORD')
    waittime = float(excuteCFG.GetConfig().getSetting('WAITTIME'))

    username_xpath = excuteCFG.GetConfig().getHomepage('username_xpath')
    password_xpath = excuteCFG.GetConfig().getHomepage('password_xpath')
    login_xpath = excuteCFG.GetConfig().getHomepage('login_xpath')

    system_setting_xpath = excuteCFG.GetConfig().getSystemSetting('system_setting_xpath')
    log_record_xpath = excuteCFG.GetConfig().getSystemSetting('log_record_xpath')

    log_record_pages_count = excuteCFG.GetConfig().getSystemSetting('log_record_pages_count')
    log_record_pages_switch_xpath = excuteCFG.GetConfig().getSystemSetting('log_record_pages_switch_xpath')
    log_record_goto_css = excuteCFG.GetConfig().getSystemSetting('log_record_goto_css')
    log_record_goto_btn_css = excuteCFG.GetConfig().getSystemSetting('log_record_goto_btn_css')

except Exception as e:

    baseinfo.getErrorInfo('获取配置文件出错')
    print e


class SystemLogRecord(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(waittime)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(url)
        self.driver.find_element_by_xpath(username_xpath).send_keys(username)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath(password_xpath).send_keys(password)
        self.driver.implicitly_wait(waittime)
        self.driver.find_element_by_xpath(login_xpath).click()
        self.driver.implicitly_wait(waittime)
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='pull-right close']")))
        self.driver.find_element_by_xpath("//button[@class='pull-right close']").click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/h1').text, u'首页概览')

    def test_logRecordPageSkip(self):

        self.driver.find_element_by_xpath(system_setting_xpath).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        self.driver.find_element_by_xpath(log_record_xpath).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        totalPages = int(self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')[5])
        curPage = int(self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')[1])
        print self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')
        print totalPages, curPage

        if totalPages == curPage:
            for i in range(0, 900, 50):
                self.driver.execute_script('document.querySelector(".box-body").scrollTop=%d' % i)
                self.driver.implicitly_wait(waittime)
                time.sleep(0.5)
        else:
            self.driver.find_element_by_css_selector(log_record_goto_css).send_keys(totalPages)
            self.driver.implicitly_wait(waittime)

            self.driver.find_element_by_css_selector(log_record_goto_btn_css).click()
            self.driver.implicitly_wait(waittime)
            time.sleep(waittime)

            # print self.driver.find_element_by_xpath(log_record_pages_switch_xpath.replace('a[%d]', 'a[2]')).get_attribute('disabled')

            self.assertTrue(self.driver.find_element_by_xpath(log_record_pages_switch_xpath.replace('a[%d]', 'a[3]')).get_attribute('disabled'))



    def test_logRecordPageSwitch(self):
        self.driver.find_element_by_xpath(system_setting_xpath).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        self.driver.find_element_by_xpath(log_record_xpath).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        totalPages = int(self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')[5])
        curPage = int(self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')[1])

        print self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')
        print totalPages, curPage

        if totalPages == curPage:
            for i in range(0, 900, 50):
                self.driver.execute_script('document.querySelector(".box-body").scrollTop=%d' % i)
                self.driver.implicitly_wait(waittime)
                time.sleep(0.5)
        else:
            for i in [4, 2, 3, 1]:

                self.driver.find_element_by_xpath(log_record_pages_switch_xpath.replace('a[%d]', 'a[%d]' % i)).click()
                self.driver.implicitly_wait(waittime)
                time.sleep(waittime)
                if i == 4 or i == 3:
                    self.assertEqual(int(self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')[1]), totalPages)
                elif i == 2:
                    self.assertEqual(int(self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')[1]), totalPages - 1)
                else:
                    self.assertEqual(int(self.driver.find_element_by_xpath(log_record_pages_count).text.split(' ')[1]), 1)

    def tearDown(self):
        self.driver.quit()














