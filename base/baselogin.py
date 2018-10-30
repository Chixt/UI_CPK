#!/usr/bin/env python
# encoding:utf-8
import sys
sys.path.append('./venv/lib/python2.7/site-packages')
from selenium import webdriver
import os
from base import excuteCFG
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import excuteCFG

cfgfile = os.path.abspath('.') + '/config.ini'  # 配置文件位置
username_xpath = excuteCFG.ConfigRead(cfgfile,'homepage','username_xpath').CfgRead()
password_xpath = excuteCFG.ConfigRead(cfgfile,'homepage','password_xpath').CfgRead()
login_xpath = excuteCFG.ConfigRead(cfgfile,'homepage','login_xpath').CfgRead()
url = excuteCFG.ConfigRead(cfgfile,'setting','CPK_URL').CfgRead()
class Login(object):

    username_xpath = excuteCFG.ConfigRead(cfgfile,'homepage','username_xpath').CfgRead()
    password_xpath = excuteCFG.ConfigRead(cfgfile,'homepage','password_xpath').CfgRead()
    login_xpath = excuteCFG.ConfigRead(cfgfile,'homepage','login_xpath').CfgRead()
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    def login(self, url, username, password, cfgfile, waittime):
        try:
            #driver = self.driver
            self.driver.maximize_window()
            self.driver.implicitly_wait(waittime)
            self.driver.get(url)
            if 'input' in self.driver.find_element_by_xpath(username_xpath).tag_name:
                pass
            else:
                raise Exception
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
        except Exception:
            pass
    def logout(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="header"]/ul/li[2]/button').click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('//*[@id="header"]/ul/li[2]/ul/li[2]/a').click()
            if 'input' in self.driver.find_element_by_xpath(username_xpath).tag_name:
                pass
            else:
                raise Exception
            self.driver.implicitly_wait(5)
            self.driver.quit()

        except Exception:
            pass





