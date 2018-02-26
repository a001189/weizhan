#!/usr/local/bin python
# -*-coding:utf-8-*-
'''
author: ysj
time: 2017/9/20 下午4:59
desc:
'''
from handlers.PageCreate import handlers

# from tornado.web import RequestHandler as Raw_RequestHandler
# from vmbsdk.web.tornado.webhandlers import RequestHandler,RestfulAPIHandler,BadRequestError
# from vmbsdk.web.tornado.webhandlers import async_func
# from tornado.httpclient import AsyncHTTPClient
# import json
# from util import MongoKit
# import re
# SUCCESSFUL_RESPONSE = {"status": 1, "msg": ""}
# class AuthBase(RestfulAPIHandler):
#     """
#     获得collogeid，enterpriseid
#     此处无验证，设定为0，0
#     """
#     collogeid,enterpriseid =0,0
#     db_name = "weizhan"
#     Mongoclient = MongoKit().client[db_name]["page_%d_%d" %(enterpriseid,collogeid)]
#
#
# class TestHander(RequestHandler):
#     def get(self, *args, **kwargs):
#         self.write("so so so")
# class TestHander2(Raw_RequestHandler):
#     def get(self):
#         self.write("so so 2222")
#
#
# class TestHander3(RestfulAPIHandler):
#     @async_func
#     def default_get(self, *args, **kwargs):
#         return {"a":"v"}
# class TestInvokeHandler(RestfulAPIHandler):
#     @async_func
#     def default_get(self):
#         result = yield AsyncHTTPClient().fetch('http://www.baidu.com')
#         print(result)
#         print(result.body)
#         return dict(test=result.body)
# class TestHander4(RestfulAPIHandler):
#     @async_func
#     def get_test5(self):
#         # test = input
#         size =self.get_argument("size","1111")
#         # self.write(size)
#         return {"status":1,"msg":"成功"}
#         # return self.size
# class PagecodeValidate(AuthBase):
#     @async_func
#     def default_get(self):
#         code = self.get_arg("code",None)
#         if code is None :
#             raise BadRequestError("code is None")
#         if  not (re.match(r"[a-zA-Z_0-9]+",code) and  3<len(code)<10):
#             raise BadRequestError("code  rules is not allowed ")
#         # dbase = MongoKit().client[self.db_dict]
#         # collection = dbase["page_%d_%d" %(self.enterpriseid,self.collogeid)].find_one({"code": code})
#         collection = self.Mongoclient.find_one({"code": code})
#
#         if collection :
#             raise BadRequestError("pagecode is exist")
#         else:
#             return SUCCESSFUL_RESPONSE
# class PageCreate(AuthBase):
#     @async_func
#     def default_get(self):
#         args={}
#         get_arg = ["code","description","indexpage","keywords","title"]
#         for  arg in get_arg:
#             args[arg] = self.get_argument(arg,"")
#         # code = self.get_argument("code","")
#         # description = self.get_argument("description","")
#         # indexpage = self.get_argument("indexpage","")
#         # keywords = self.get_argument("keywords","")
#         # title = self.get_argument("title","")
#         if 4 >= len(args["title"]) or len(args["title"]) >= 60:
#             raise BadRequestError("title length is not right")
#         dbase = MongoKit().client[self.db_dict]
#         collection = dbase["page_%d_%d" % (self.enterpriseid, self.collogeid)].insert(args)
#         if collection:
#             return SUCCESSFUL_RESPONSE
#         else:
#             raise BadRequestError("save failed")
# class Test(RestfulAPIHandler):
#     def default_get(self,*arg,**kwargs):
#         #name = self.arg
#         #self.check_name(name)?
#         a={}
#         body =self.request.query_arguments
#         body2=self.request.arguments
#         for  arg in body:
#             a[arg] = self.get_arg(arg,"ss")
#         return a
#     def default_post(self,body):
#         print(body)
#         return {"da":"sda"}
#
#     def check_name(self, name):
#         if not name:
#             raise BadRequestError
#         elif not isinstance(name, str):
#             raise BadRequestError
#         elif len(name) > 10:
#             raise BadRequestError
#
#
# handlers = [
#     (r"/test2",TestHander2),
#     (r"/test1",TestHander),
#     (r"/test3",TestHander3),
#
#     (r"/tests",TestInvokeHandler),
#     (r"/pagecode",PagecodeValidate),
#     (r"/test4",TestHander4),
#     (r"/pagecreate",PageCreate),
#     (r"/test6/",Test),
#
# ]
