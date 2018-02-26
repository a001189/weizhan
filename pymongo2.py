#!/usr/local/bin python
# -*-coding:utf-8-*-
'''
author: ysj
time: 2017/9/20 下午8:53
desc:
'''
import pymongo
def mongoconnect(username="root",password="Vmobel2016",host="localhost",port=27017):

     return pymongo.MongoClient('mongodb://{user}:{password}@{host}:{port}'.format(
        user=username, password=password, host=host, port=port), maxPoolSize=10)