#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : Sam Zhou
date   : 2017/9/13 10:59
role   : Version Update
'''

from vmbsdk.web.tornado.application import Application as App

from handlers import handlers


class Application(App):
    def __init__(self, **settings):
        super(Application, self).__init__(handlers, **settings)
