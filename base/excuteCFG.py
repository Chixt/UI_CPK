#!/usr/bin/env python
# encoding:utf-8
import sys

sys.path.append('./venv/lib/python2.7/site-packages')
import ConfigParser

conf = ConfigParser.ConfigParser(allow_no_value=True)
conf.read('./config.ini')


# conf.read('../../config.ini')

class ConfigRead(object):
    def __init__(self, file, item, section):
        self.file = file
        self.item = item
        self.section = section

    def CfgRead(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.file)

            return config.get(self.item, self.section)
        except Exception, e:
            pass


class GetConfig:

    def __init__(self):
        pass

    def getSetting(self, sectionName):
        return conf.get('setting', sectionName)

    def getHomepage(self, sectionName):
        return conf.get('homepage', sectionName)

    def getAppManagement(self, sectionName):
        return conf.get('appmanagement', sectionName)

    def getPresetInfo(self, sectionName):
        return conf.get('preset', sectionName)

    def getSystemSetting(self,sectionName):
        return conf.get('system', sectionName)

class ConfigWrite(object):

    def __init__(self, file, item, section, value):
        self.file = file
        self.item = item
        self.section = section
        self.value = value

    def CfgWrite(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.cfgfile)
            config.set(self.section, self.item, self.value)
            config.write(open(self.cfgfile, 'w'))
        except Exception, e:
            pass
