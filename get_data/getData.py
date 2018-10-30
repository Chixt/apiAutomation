#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:ChiXiaotong
@file:getData.py
@project:apiAutomation
@software:PyCharm
@time:2018/10/30 上午10:21
"""


import xlrd
from base import getConfig

datafile = getConfig.getSetting('datafile')


df = xlrd.open_workbook(datafile)




