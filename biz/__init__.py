#!/usr/local/bin python
# -*-coding:utf-8-*-
'''
author: ysj
time: 2017/9/21 上午10:32
desc: mongo
'''

from util import MongoKit
from vmbsdk.tools import singleton
from vmbsdk.errors import BadRequestError, ServiceNotImplementedError
@singleton
class Wizhan():
    def __int__(self):
        self._db = None
    @property
    def db(self):
        if self._db is  None:
            self._db = MongoKit().client['weizhan']
        return self._db
    def insert_one(self, doc):
        raise ServiceNotImplementedError

    def insert_many(self, doc_list):
        raise ServiceNotImplementedError

    def update_one(self, filter, updater):
        raise ServiceNotImplementedError

    def update_many(self, filter, updater):
        raise ServiceNotImplementedError

    def delete_one(self, filter):
        raise ServiceNotImplementedError

    def delete_many(self, filter):
        raise ServiceNotImplementedError

    def find_one(self, filter, projection=None):
        raise ServiceNotImplementedError

    def find(self, filter, projection=None):
        raise ServiceNotImplementedError

