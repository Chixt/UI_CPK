#!/usr/bin/env python
# encoding:utf-8
"""应用排行分析查看，点击跳转"""

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
    username_xpath = excuteCFG.ConfigRead(cfgfile, 'homepage', 'username_xpath').CfgRead()
    password_xpath = excuteCFG.ConfigRead(cfgfile, 'homepage', 'password_xpath').CfgRead()
    login_xpath = excuteCFG.ConfigRead(cfgfile, 'homepage', 'login_xpath').CfgRead()
    '''应用排行分析-安装'''
    install = excuteCFG.ConfigRead(cfgfile, 'homepage', 'install_xpath').CfgRead()
    install_1 = excuteCFG.ConfigRead(cfgfile, 'homepage', 'install_xpath_1').CfgRead()
    '''应用排行分析-卸载'''
    uninstall = excuteCFG.ConfigRead(cfgfile, 'homepage', 'uninstall_xpath').CfgRead()
    uninstall_1 = excuteCFG.ConfigRead(cfgfile, 'homepage', 'uninstall_xpath_1').CfgRead()
    '''应用排行分析-升级'''
    update = excuteCFG.ConfigRead(cfgfile, 'homepage', 'update_xpath').CfgRead()
    update_1 = excuteCFG.ConfigRead(cfgfile, 'homepage', 'update_xpath_1').CfgRead()
    '''应用排行分析-评分'''
    score = excuteCFG.ConfigRead(cfgfile, 'homepage', 'score_xpath').CfgRead()
    score_1 = excuteCFG.ConfigRead(cfgfile, 'homepage', 'score_xpath_1').CfgRead()
    '''导航窗口，首页'''
    homepage = excuteCFG.ConfigRead(cfgfile, 'dashboard', 'homepage').CfgRead()
    '''应用详情页面头'''
    title = excuteCFG.ConfigRead(cfgfile, 'application management', 'title').CfgRead()
    '''最新应用导入'''
    new_import = excuteCFG.ConfigRead(cfgfile, 'homepage', 'new_import').CfgRead()
    '''客户端最新动态'''
    client = excuteCFG.ConfigRead(cfgfile, 'homepage', 'client').CfgRead()
except IOError, e:
    baseinfo.getErrorInfo('获取配置文件异常')


class HomePage(unittest.TestCase):

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

    def test_rank_analyse(self):

        # 应用安装分析（左下角）
        self.driver.find_element_by_xpath(install).click()
        # 依次点击安装动态中的应用名称：1，3，5，7，9
        for i in range(1, 10, 2):
            # print i
            self.driver.find_element_by_xpath(install_1.replace('tr[i]', 'tr[%d]' % i)).click()
            self.driver.implicitly_wait(waittime)
            '''
            断言问题
            self.assertEqual(self.driver.find_element_by_xpath(title).text,u'非托管应用')
            '''
            self.driver.find_element_by_xpath(homepage).click()
            self.driver.implicitly_wait(waittime)

        for j in range(1, 10, 2):
            self.driver.find_element_by_xpath(update).click()
            self.driver.find_element_by_xpath(update_1.replace('tr[i]', 'tr[%d]' % j)).click()
            self.driver.implicitly_wait(waittime)
            '''
            断言问题
            self.assertEqual(self.driver.find_element_by_xpath(title).text, u'非托管应用')
            '''
            self.driver.find_element_by_xpath(homepage).click()
            self.driver.implicitly_wait(waittime)

        for k in range(1, 10, 2):
            self.driver.find_element_by_xpath(score).click()
            self.driver.find_element_by_xpath(score_1.replace('tr[i]', 'tr[%d]' % k)).click()
            self.driver.implicitly_wait(waittime)
            '''
            断言问题
            self.assertEqual(self.driver.find_element_by_xpath(title).text, u'非托管应用')
            '''
            self.driver.find_element_by_xpath(homepage).click()
            self.driver.implicitly_wait(waittime)

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
