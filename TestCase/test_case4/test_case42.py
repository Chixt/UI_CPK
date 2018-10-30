#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:ChiXiaotong
@file:test_case42.py
@project:UI_CPK
@software:PyCharm
@time:2018/10/16 上午11:25
"""

from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base import excuteCFG, baseinfo
import time

try:

    url = excuteCFG.GetConfig().getSetting('CPK_URL')
    username = excuteCFG.GetConfig().getSetting('USERNAME')
    password = excuteCFG.GetConfig().getSetting('PASSWORD')
    waittime = excuteCFG.GetConfig().getSetting('WAITTIME')

    username_xpath = excuteCFG.GetConfig().getHomepage('username_xpath')
    password_xpath = excuteCFG.GetConfig().getHomepage('password_xpath')
    login_xpath = excuteCFG.GetConfig().getHomepage('login_xpath')

    preset_option_xpath = excuteCFG.GetConfig().getPresetInfo('preset_option_xpath')

    preset_quick_launch_list_xpath = excuteCFG.GetConfig().getPresetInfo('preset_quick_launch_list_xpath')

    preset_quick_launch_add_xpath = excuteCFG.GetConfig().getPresetInfo('preset_quick_launch_add_xpath')
    preset_quick_launch_add_item_xpath = excuteCFG.GetConfig().getPresetInfo('preset_quick_launch_add_item_xpath')

    preset_quick_launch_del_css = excuteCFG.GetConfig().getPresetInfo('preset_quick_launch_del_css')

    preset_quick_launch_add_confirm_css = excuteCFG.GetConfig().getPresetInfo('preset_quick_launch_add_confirm_css')

    preset_save_css = excuteCFG.GetConfig().getPresetInfo('preset_save_css')

except IOError, e:
    # pass
    baseinfo.getErrorInfo(u'获取配置文件异常')


class Login(unittest.TestCase):

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
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/h1').text, u'首页概览')

        self.driver.find_element_by_xpath(preset_option_xpath).click()
        self.driver.implicitly_wait(waittime)
        time.sleep(3)

    def test_presetQuickLaunchAdd(self):

        if self.driver.find_element_by_xpath(
                '%s[6]/h6' % preset_quick_launch_list_xpath).text.strip() == u'添加应用':
            for i in range(2, 6):
                if self.driver.find_element_by_xpath(
                        '%s[%d]/h6' % (preset_quick_launch_list_xpath, i)).text.strip() == '':
                    print 'i = %d' % i
                    break
                else:
                    pass

            self.driver.find_element_by_xpath(preset_quick_launch_add_xpath).click()
            self.driver.implicitly_wait(waittime)
            time.sleep(3)
            if self.driver.find_element_by_xpath(
                    preset_quick_launch_add_item_xpath).text.strip() == u'未找到相关应用':
                print u'无应用可添加'
                self.driver.find_element_by_css_selector('.layui-layer-ico').click()
                self.driver.implicitly_wait(waittime)

            else:
                chosenItem = self.driver.find_element_by_xpath('%s[3]' % preset_quick_launch_add_item_xpath).text.strip()
                print chosenItem
                self.driver.find_element_by_xpath('%s[4]/input' % preset_quick_launch_add_item_xpath).send_keys(Keys.SPACE)

                self.driver.implicitly_wait(waittime)

                self.driver.find_element_by_css_selector(preset_quick_launch_add_confirm_css).click()
                self.driver.implicitly_wait(waittime)

                self.driver.find_element_by_css_selector(preset_save_css).click()
                self.driver.implicitly_wait(waittime)
                time.sleep(3)

                self.driver.find_element_by_xpath(preset_option_xpath).click()
                self.driver.implicitly_wait(waittime)
                time.sleep(3)

                print self.driver.find_element_by_xpath(
                    '%s[%d]/h6' % (preset_quick_launch_list_xpath, i)).text.strip()
                self.assertIsNotNone(self.driver.find_element_by_xpath(
                    '%s[%d]/h6' % (preset_quick_launch_list_xpath, i)).text.strip())
        else:
            print u'预置已满'


    def test_presetQuickLaunchDel(self):

        if self.driver.find_element_by_xpath('%s[2]/h6' % preset_quick_launch_list_xpath).text.strip() == '':
            print u'暂无预置应用，不可进行删除操作。'
        else:

            for i in range(2, 7):
                if u'exemplar' in self.driver.find_element_by_xpath('//*[@id="botpad"]/tbody/tr/td[%d]/div' % i).get_attribute('class'):
                    pass
                else:
                    break
            print i
            delItem = self.driver.find_element_by_xpath('%s[2]/h6' % preset_quick_launch_list_xpath).text.strip()
            self.driver.implicitly_wait(waittime)
            time.sleep(3)
            #self.driver.find_element_by_css_selector('td.app-frame:nth-child(2) > div:nth-child(1) > span:nth-child(2) > a:nth-child(1)').click()
            self.driver.execute_script(
                'document.querySelector(\"%s\").removeAttribute(\"hidden\");' % preset_quick_launch_del_css)
            self.driver.implicitly_wait(waittime)
            time.sleep(3)
            self.driver.find_element_by_css_selector(preset_quick_launch_del_css).click()
            self.driver.implicitly_wait(waittime)
            self.driver.find_element_by_css_selector(preset_save_css).click()
            self.driver.implicitly_wait(waittime)
            time.sleep(3)

            self.driver.find_element_by_xpath(preset_option_xpath).click()
            self.driver.implicitly_wait(waittime)
            time.sleep(3)

            print self.driver.find_element_by_xpath(
                '%s[2]/h6' % preset_quick_launch_list_xpath).text.strip()
            self.assertIn(u'blank', self.driver.find_element_by_xpath('//*[@id="botpad"]/tbody/tr/td[%d]/div' % (i-1)).get_attribute('class'))

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



























