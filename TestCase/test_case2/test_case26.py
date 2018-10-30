#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:ChiXiaotong
@file:test_case26.py
@project:UI_CPK
@software:PyCharm
@time:2018/10/19 上午10:41
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

    client_state_all_css = excuteCFG.GetConfig().getHomepage('client_state_all_css')
    client_state_option_filter_xpath = excuteCFG.GetConfig().getHomepage('client_state_option_filter_xpath')
    client_state_option_items_xpath = excuteCFG.GetConfig().getHomepage('client_state_option_items_xpath')
    client_state_list_xpath = excuteCFG.GetConfig().getHomepage('client_state_list_xpath')
    client_state_pages_xpath = excuteCFG.GetConfig().getHomepage('client_state_pages_xpath')


except Exception as e:
    baseinfo.getErrorInfo('获取配置文件出错')
    print e


class AllClientState(unittest.TestCase):

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

    def test_homepageAllClientStateFilter(self):

        self.driver.find_element_by_css_selector(client_state_all_css).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        if self.driver.find_element_by_xpath(client_state_list_xpath.replace('tr[%d]/td[5]', 'tr/td')).text == u'筛选结果为空':

            print u'暂无应用客户端动态'

        else:

            for i in range(2, len(self.driver.find_elements(By.XPATH, client_state_option_items_xpath.replace('dd[%d]', 'dd'))) + 1):

                self.driver.find_element_by_xpath(client_state_option_filter_xpath).click()
                self.driver.implicitly_wait(waittime)
                time.sleep(waittime)

                chosenItem = self.driver.find_element_by_xpath(client_state_option_items_xpath.replace('dd[%d]', 'dd[%d]' % i)).text.strip()
                self.driver.find_element_by_xpath(client_state_option_items_xpath.replace('dd[%d]', 'dd[%d]' % i)).click()
                self.driver.implicitly_wait(waittime)
                time.sleep(waittime)

                if self.driver.find_element_by_xpath(
                        client_state_list_xpath.replace('tr[%d]/td[5]', 'tr/td')).text == u'筛选结果为空':
                    print u'筛选结果为空，此分类下无动态'
                else:
                    for j in range(1, len(self.driver.find_elements(By.XPATH, client_state_list_xpath.replace('tr[%d]/td[5]', 'tr'))) + 1):
                        self.assertEqual(self.driver.find_element_by_xpath(client_state_list_xpath.replace('tr[%d]', 'tr[%d]' % i)).text, chosenItem)

    def test_homepageAllClientStatePageSwitch(self):

        self.driver.find_element_by_css_selector(client_state_all_css).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        if self.driver.find_element_by_xpath(client_state_pages_xpath.replace('li[%d]', 'li')) <= 5:
            print u'无需翻页，无页可翻'

        else:

            for i in range(0, 900, 50):
                self.driver.execute_script('document.querySelector(".box-body").scrollTop=%d' % i)
                self.driver.implicitly_wait(waittime)
                time.sleep(0.5)

            pagecount = len(self.driver.find_elements(By.XPATH, client_state_pages_xpath.replace('li[%d]', 'li')))

            for k, i in enumerate([pagecount, 1, pagecount - 1, 2, 4, 3]):

                self.driver.find_element_by_xpath(client_state_pages_xpath.replace('li[%d]', 'li[%d]/a' % i)).click()
                self.driver.implicitly_wait(waittime)
                time.sleep(waittime)
                self.driver.execute_script('document.querySelector(".box-body").scrollTop=1000')
                time.sleep(waittime)

                if k % 2 == 0:
                    if k == 0:
                        self.assertEqual(self.driver.find_element_by_xpath(client_state_pages_xpath.replace('li[%d]', 'li[%d]' % pagecount)).get_attribute('class'), 'paginate_button last disabled')
                    else:
                        self.assertEqual(
                            self.driver.find_element_by_xpath(client_state_pages_xpath.replace('li[%d]', 'li[4]')).get_attribute('class'),
                            'paginate_button active')
                else:
                    self.assertEqual(
                        self.driver.find_element_by_xpath(client_state_pages_xpath.replace('li[%d]', 'li[1]')).get_attribute('class'),
                        'paginate_button first disabled')
            # time.sleep(3)

            time.sleep(0.1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()







