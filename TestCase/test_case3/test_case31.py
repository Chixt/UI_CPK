#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:ChiXiaotong
@file:test_case31.py
@project:UI_CPK
@software:PyCharm
@time:2018/9/25 上午10:32
"""

from selenium import webdriver
import unittest
from base import excuteCFG, baseinfo
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

    appManagement_xpath = excuteCFG.GetConfig().getAppManagement('appmanagement_xpath')
    hostedApp_xpath = excuteCFG.GetConfig().getAppManagement('hostedapp_xpath')
    legacyApp_xpath = excuteCFG.GetConfig().getAppManagement('legacyapp_xpath')

    desktopTab_xpath = excuteCFG.GetConfig().getAppManagement('desktoptab_xpath')

    desktop_classification_xpath = excuteCFG.GetConfig().getAppManagement('desktop_classification_xpath')
    desktop_classification_items_xpath = excuteCFG.GetConfig().getAppManagement('desktop_classification_items_xpath')
    desktop_status_xpath = excuteCFG.GetConfig().getAppManagement('desktop_status_xpath')
    desktop_status_items_xpath = excuteCFG.GetConfig().getAppManagement('desktop_status_items_xpath')
    desktop_security_xpath = excuteCFG.GetConfig().getAppManagement('desktop_security_xpath')
    desktop_security_items_xpath = excuteCFG.GetConfig().getAppManagement('desktop_security_items_xpath')

    desktop_applist_xpath = excuteCFG.GetConfig().getAppManagement('desktop_applist_xpath')
    desktop_app_pages_xpath = excuteCFG.GetConfig().getAppManagement('desktop_app_pages_xpath')

    webTab_xpath = excuteCFG.GetConfig().getAppManagement('webtab_xpath')
    desktop_appdetails_back_xpath = excuteCFG.GetConfig().getAppManagement('desktop_appdetails_back_xpath')

    desktop_app_sort_xpath = excuteCFG.GetConfig().getAppManagement('desktop_app_sort_xpath')

except Exception as e:
    baseinfo.getErrorInfo('获取congfig.ini配置文件setting出错')
    print e


class DesktopAppManagement(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
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
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/h1').text, u'首页概览')

        time.sleep(waittime)

        self.driver.find_element_by_xpath(appManagement_xpath).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)

        self.driver.find_element_by_xpath(hostedApp_xpath).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(waittime)


    def test_switchAppManagement(self):

        self.driver.find_element_by_xpath(desktopTab_xpath).click()
        self.driver.implicitly_wait(waittime)

        self.driver.find_element_by_xpath(webTab_xpath).click()
        self.driver.implicitly_wait(waittime)

    def test_desktopAppClassificationFilter(self):

        self.driver.find_element_by_xpath(desktopTab_xpath).click()
        self.driver.implicitly_wait(waittime)

        # 应用分类-办公游戏等

        if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
            print '筛选结果为空'
            pass
        else:

            for i in range(2, len(self.driver.find_elements(By.XPATH, desktop_classification_items_xpath)) + 1):
                self.driver.find_element_by_xpath(desktop_classification_xpath).click()
                self.driver.implicitly_wait(waittime)
                chosenItem = self.driver.find_element_by_xpath(
                    desktop_classification_items_xpath + '[%s]' % i).text.strip()
                self.driver.find_element_by_xpath(desktop_classification_items_xpath + '[%s]' % i).click()
                self.driver.implicitly_wait(waittime)
                if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
                    print '筛选结果为空'
                else:
                    for j in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):
                        # print chosenItemText + 'kjhsdfkhadsadfasdfasdf'
                        self.assertIn(chosenItem, self.driver.find_element_by_xpath(
                            '%s[%d]/td[5]/span' % (desktop_applist_xpath, j)).get_attribute('title'))
                        # print '%s[%d]/td[10]' % (desktop_applist_xpath, j)
                        # print type(self.driver.find_element_by_xpath('%s[%d]/td[10]' % (desktop_applist_xpath, j)).text)
                        self.driver.implicitly_wait(waittime)

    def test_desktopAppStatusFilter(self):

        self.driver.find_element_by_xpath(desktopTab_xpath).click()
        self.driver.implicitly_wait(waittime)

        # 应用上下架状态

        if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
            print '筛选结果为空'
            pass
        else:
            for i in range(2, len(self.driver.find_elements(By.XPATH, desktop_status_items_xpath)) + 1):
                self.driver.find_element_by_xpath(desktop_status_xpath).click()
                self.driver.implicitly_wait(waittime)
                chosenItem = self.driver.find_element_by_xpath(
                    desktop_status_items_xpath + '[%s]' % i).text.strip()
                self.driver.find_element_by_xpath(desktop_status_items_xpath + '[%s]' % i).click()
                self.driver.implicitly_wait(waittime)
                if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
                    print '筛选结果为空'
                else:
                    for j in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):
                        self.assertEqual(chosenItem, self.driver.find_element_by_xpath(
                            '%s[%d]/td[12]' % (desktop_applist_xpath, j)).text)
                        self.driver.implicitly_wait(waittime)

            '''
            for i in self.driver.find_elements(By.XPATH, desktop_status_items_xpath):
                self.driver.find_element_by_xpath(desktop_status_xpath).click()
                self.driver.implicitly_wait(waittime)
                chosenItem = i.text
                i.click()
                self.driver.implicitly_wait(waittime)
                if chosenItem == u'全部':
                    print '筛选全部'
                    pass
                elif self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
                    print '筛选结果为空'
                    pass
                else:
                    for j in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):
                        self.assertEqual(chosenItem, self.driver.find_element_by_xpath(
                            '%s[%d]/td[12]' % (desktop_applist_xpath, j)).text)
                        self.driver.implicitly_wait(waittime)
'''

    def test_desktopAppSecurityFilter(self):

        self.driver.find_element_by_xpath(desktopTab_xpath).click()
        self.driver.implicitly_wait(waittime)

        # 应用密级-秘密机密等。
        if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
            print '筛选结果为空'
            pass
        else:
            for i in range(2, len(self.driver.find_elements(By.XPATH, desktop_security_items_xpath)) + 1):
                self.driver.find_element_by_xpath(desktop_security_xpath).click()
                self.driver.implicitly_wait(waittime)
                chosenItem = self.driver.find_element_by_xpath(
                    desktop_security_items_xpath + '[%s]' % i).text.strip()
                self.driver.find_element_by_xpath(desktop_security_items_xpath + '[%s]' % i).click()
                self.driver.implicitly_wait(waittime)
                if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
                    print '筛选结果为空'
                else:
                    for j in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):
                        self.assertEqual(chosenItem, self.driver.find_element_by_xpath(
                            '%s[%d]/td[10]' % (desktop_applist_xpath, j)).text)
                        self.driver.implicitly_wait(waittime)

            '''
            for i in self.driver.find_elements(By.XPATH, desktop_security_items_xpath):
                self.driver.find_element_by_xpath(desktop_security_xpath).click()
                self.driver.implicitly_wait(waittime)
                chosenItem = i.text
                i.click()
                self.driver.implicitly_wait(waittime)
                if chosenItem == u'全部':
                    print '筛选全部'
                    pass
                elif self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
                    print '筛选结果为空'
                    pass
                else:
                    for j in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):
                        self.assertEqual(chosenItem, self.driver.find_element_by_xpath(
                            '%s[%d]/td[10]' % (desktop_applist_xpath, j)).text)
                        self.driver.implicitly_wait(waittime)
'''

    def test_desktopAppPageSwitch(self):

        self.driver.find_element_by_xpath(desktopTab_xpath).click()
        self.driver.implicitly_wait(waittime)

        # 桌面应用翻页。
        if len(self.driver.find_elements(By.XPATH, desktop_app_pages_xpath)) <= 5:
            print len(self.driver.find_elements(By.XPATH, desktop_app_pages_xpath))
            print '无需翻页，无页可翻'
            pass

        else:
            self.driver.execute_script('document.querySelector(".well").scrollTop=100000')
            self.driver.implicitly_wait(waittime)
            for k, i in enumerate([len(self.driver.find_elements(By.XPATH, desktop_app_pages_xpath)), 1,
                                   len(self.driver.find_elements(By.XPATH, desktop_app_pages_xpath)) - 1, 2, 4, 1]):

                self.driver.find_element_by_xpath('%s[%d]/a' % (desktop_app_pages_xpath, i)).click()
                self.driver.implicitly_wait(waittime)

                if k % 2 == 0:
                    if k == 0:
                        self.assertEqual(self.driver.find_element_by_xpath('%s[%d]' % (desktop_app_pages_xpath, len(
                            self.driver.find_elements(By.XPATH, desktop_app_pages_xpath)))).get_attribute('class'),
                                         'paginate_button last disabled')
                    else:
                        self.assertEqual(
                            self.driver.find_element_by_xpath('%s[4]' % desktop_app_pages_xpath).get_attribute('class'),
                            'paginate_button active')
                else:
                    self.assertEqual(
                        self.driver.find_element_by_xpath('%s[1]' % desktop_app_pages_xpath).get_attribute('class'),
                        'paginate_button first disabled')

    def test_desktopAppDetails(self):

        self.driver.find_element_by_xpath(desktopTab_xpath).click()
        self.driver.implicitly_wait(waittime)

        if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
            print '筛选结果为空'
            pass
        else:
            for i in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):
                # 跳转到应用详情页面

                self.driver.find_element_by_xpath('%s[%d]/td[13]/a' % (desktop_applist_xpath, i)).click()
                self.driver.implicitly_wait(waittime)
                self.assertTrue(self.driver.find_element_by_xpath(desktop_appdetails_back_xpath))
                self.driver.find_element_by_xpath(desktop_appdetails_back_xpath).click()
                self.driver.implicitly_wait(waittime)
                self.assertTrue(self.driver.find_element_by_xpath('%s[%d]/td[13]/a' % (desktop_applist_xpath, i)))

    def test_desktopAppSort(self):

        self.driver.find_element_by_xpath(desktopTab_xpath).click()
        self.driver.implicitly_wait(waittime)

        if self.driver.find_element_by_xpath('//*[@id="software_list"]/tr/td').text == u'筛选结果为空':
            print '筛选结果为空'
            pass

        else:

            for m in [6, 7, 8]:
                size = []
                self.driver.find_element_by_xpath('%s[%d]' % (desktop_app_sort_xpath, m)).click()
                self.driver.implicitly_wait(waittime)

                if len(self.driver.find_elements(By.XPATH, desktop_app_pages_xpath)) == 5:

                    for j in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):

                        if 'KB' in self.driver.find_element_by_xpath(
                                '%s[%d]/td[%d]' % (desktop_applist_xpath, j, m)).text:

                            size.append(float(self.driver.find_element_by_xpath(
                                '%s[%d]/td[%d]' % (desktop_applist_xpath, j, m)).text.split()[0]) / 1024)

                        else:

                            size.append(float(
                                self.driver.find_element_by_xpath(
                                    '%s[%d]/td[%d]' % (desktop_applist_xpath, j, m)).text.split()[0]))

                else:

                    for i in range(3, len(self.driver.find_elements(By.XPATH, desktop_app_pages_xpath)) - 1):

                        self.driver.find_element_by_xpath('%s[%d]/a' % (desktop_app_pages_xpath, i)).click()

                        for j in range(1, len(self.driver.find_elements(By.XPATH, desktop_applist_xpath)) + 1):
                            if 'KB' in self.driver.find_element_by_xpath(
                                    '%s[%d]/td[%d]' % (desktop_applist_xpath, j, m)).text:
                                size.append(float(
                                    self.driver.find_element_by_xpath(
                                        '%s[%d]/td[%d]' % (desktop_applist_xpath, j, m)).text.split()[0]) / 1024)
                            else:
                                size.append(
                                    float(self.driver.find_element_by_xpath(
                                        '%s[%d]/td[%d]' % (desktop_applist_xpath, j, m)).text.split()[0]))

                if self.driver.find_element_by_xpath('%s[%d]' % (desktop_app_sort_xpath, m)).get_attribute(
                        'aria-sort') == 'ascending':

                    # 从list[1]开始向后

                    for k, i in enumerate(size[1:]):
                        self.assertTrue(size[k] <= i)

                else:

                    for k, i in enumerate(size[1:]):
                        self.assertTrue(size[k] >= i)

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


if __name__ == "__main__":
    unittest.main()
