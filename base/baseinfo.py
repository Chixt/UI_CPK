#!/usr/bin/env python
#-*- coding: utf-8 -*-
import logging
import logging.handlers
import time
import os
#LogPath = os.path.abspath('..')

#print LogPath
now = time.strftime("%Y-%m-%d")
#filename = LogPath+'/UI_CPK/log/'+now + '.log'
filename = '/Users/chi/workwork/UI_CPK/log/' + now + '.log'
file = filename
handler = logging.handlers.RotatingFileHandler(file, maxBytes=10240 * 10240, backupCount=5)#输出到日志文件
handler.setLevel(logging.INFO)
ControlPannel = logging.StreamHandler()  # 输出至控制台
ControlPannel.setLevel(logging.INFO)
fmt = '%(asctime)s - %(filename)s : %(lineno)s - %(message)s'  # 格式
formatter = logging.Formatter(fmt)  # 日志格式
handler.setFormatter(formatter)  # 文件格式
ControlPannel.setFormatter(formatter)  # 控制台格式
logger = logging.getLogger("mylogger")
logger.addHandler(handler)
logger.addHandler(ControlPannel)
logger.setLevel(logging.INFO)


def getInfo(strname):
    logger.info(strname)
def getErrorInfo(strname):
    logger.error(strname)
def getDebug(strname):
    logger.debug(strname)