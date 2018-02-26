#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : Sam Zhou
date   : 2017/9/15 14:02
role   : Version Update
'''
import pymongo
from vmbsdk.configs import configs
from vmbsdk.tools import singleton


SUCCESSFUL_RESPONSE = {"status": 1, "msg": ""}

@singleton
class MongoKit(object):

    def __init__(self):
        self._client = None
        self._unsafe_client = None

    @property
    def client(self):
        if self._client is None:
            username = configs['mongodbs']['username']
            password = configs['mongodbs']['password']
            host = configs['mongodbs']['host']
            port = configs['mongodbs']['port']
            self._client = pymongo.MongoClient('mongodb://{user}:{password}@{host}:{port}'.format(
                user=username, password=password, host=host, port=port), maxPoolSize=10)
        return self._client

    @property
    def unsafe_client(self):
        if self._unsafe_client is None:
            username = configs['mongodbs']['username']
            password = configs['mongodbs']['password']
            host = configs['mongodbs']['host']
            port = configs['mongodbs']['port']
            self._unsafe_client = pymongo.MongoClient('mongodb://{user}:{password}@{host}:{port}'.format(
                user=username, password=password, host=host, port=port), maxPoolSize=10, w=0)
        return self._unsafe_client
