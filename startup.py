#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : Sam Zhou
date   : 2017/9/13 10:40
role   : Version Update
'''
import os

from vmbsdk.configs import configs
from vmbsdk.constants.consts import const
from vmbsdk.program import MainProgram
from application import Application


class Program(MainProgram):
    def __init__(self, process_id=''):
        self.__app = None
        ini_file = os.path.join(os.path.dirname(__file__), 'settings.ini')
        settings = {}
        if os.path.exists(ini_file):
            configs.import_ini(ini_file)
            self.import_dict(settings, configs)
            configs.clear()
        else:
            from settings import settings as app_settings
            settings = app_settings
        settings[const.LOG_PATH] = settings['log_path']
        self.__app = Application(**settings)

        super(Program, self).__init__(process_id)

        self.__app.start_server()

    def import_dict(self, settings, configs):
        for k, v in configs.items():
            settings[k] = v


if __name__ == '__main__':
    MainProgram.run(Program)