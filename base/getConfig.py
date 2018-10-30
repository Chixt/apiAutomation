#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:ChiXiaotong
@file:getConfig.py
@project:apiAutomation
@software:PyCharm
@time:2018/10/30 上午10:53
"""


import ConfigParser

configfile = '/Users/chi/workwork/apiAutomation/config.ini'

config = ConfigParser.ConfigParser()
config.read(configfile)


def getSetting(key):
    config.get('setting', key)















