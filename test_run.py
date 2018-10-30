#!/usr/bin/env python
# encoding:utf-8
import sys

sys.path.append('./venv/lib/python2.7/site-packages')
import unittest
import HTMLTestRunner
import time


def creatsuite():
    testsuite = unittest.TestSuite()
    test_dir = './TestCase'
    # test_dir = '/Users/fanglujie/Documents/Project/UI_CPK/TestCase/test_case2'
    discovery = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for testcase in discovery:
        testsuite.addTests(testcase)
    return testsuite


now = time.strftime('%Y-%m-%d %H_%M_%S')
filename = './result/result%s.html' % now
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'应用商店分中心测试报告', description=u'用例执行情况:')

if __name__ == '__main__':
    allTestNames = creatsuite()
    runner.run(allTestNames)
    fp.close()
