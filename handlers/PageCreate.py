#!/usr/local/bin python
# -*-coding:utf-8-*-
'''
author: ysj
time: 2017/9/22 上午9:48
desc:
'''
from tornado.web import RequestHandler as Raw_RequestHandler
from vmbsdk.web.tornado.webhandlers import RequestHandler,RestfulAPIHandler,BadRequestError
from vmbsdk.web.tornado.webhandlers import async_func
from tornado.httpclient import AsyncHTTPClient
import json
from vmbsdk.errors import UnsupportMediaType
from util import MongoKit
import re
SUCCESSFUL_RESPONSE = {"status": 1, "msg": ""}
class AuthBase(RestfulAPIHandler):
    """
    获得collogeid，enterpriseid
    此处无验证，设定为0，0
    """
    collogeid,enterpriseid =0,0
    db_name = "weizhan"
    @property
    def Mongopage(self):
        Mongoclient = MongoKit().client[self.db_name]["page_%d_%d" %(self.enterpriseid,self.collogeid)]
        return Mongoclient
    @property
    def Mongosection(self):
        Mongoclient = MongoKit().client[self.db_name]["section_%d_%d" %(self.enterpriseid,self.collogeid)]
        return Mongoclient
    @property
    def Mongopage(self):
        Mongoclient = MongoKit().client[self.db_name]["page_%d_%d" %(self.enterpriseid,self.collogeid)]
        return Mongoclient
    @property
    def Mongocontainer(self):
        Mongoclient = MongoKit().client[self.db_name]["container_%d_%d" %(self.enterpriseid,self.collogeid)]
        return Mongoclient
    @property
    def Mongomodule(self):
        Mongoclient = MongoKit().client[self.db_name]["module_%d_%d" %(self.enterpriseid,
                                                                   self.collogeid)]
        return Mongoclient
    @property
    def Mongolayout(self):
        Mongoclient = MongoKit().client[self.db_name]["layout"]
        return Mongoclient
    @property
    def Mongodata_source(self):
        Mongoclient = MongoKit().client[self.db_name]["layout_container"]
        return Mongoclient
    @property
    def Mongocollection(self):
        Mongoclient = MongoKit().client[self.db_name]
        return Mongoclient

class PageCreate(AuthBase):
    def get_test(self):
        test = self.get_arg("code","aha")
        print(test)
        self.Mongopage.insert_one({"code":test})
        self.write(test)
        # return SUCCESSFUL_RESPONSE
    def get_codevalidate(self):
        code = self.get_arg("code","").strip()
        if re.match(r"^[0-9A-Za-z_]{4,10}$",code):
            if  not self.Mongopage.find_one({"code":code}) :
                return SUCCESSFUL_RESPONSE
            else:
                raise BadRequestError("the page code is exist")
        else:
            raise BadRequestError("the page code is not allowed")
    def get_page(self):
        """
            {
    'code':'index',
    'title':'首页',
    'description':'交行上分新员工学院',
    'keywords':'交行，新员工，学习',
    'indexpage':true
}
        :return:
        """
        paged = {}
        code = self.get_arg("code", "").strip()
        if re.match(r"^[0-9A-Za-z_]{4,10}$", code):
            if not self.Mongopage.find_one({"code": code}):
                paged["code"] = code
            else:
                raise BadRequestError("the page code is exist")
        else:
            raise BadRequestError("the page code is not allowed")
        title = self.get_arg("title","")
        if re.match(r"^.{4,60}$", code):
            paged["title"] = title
        else:
            raise BadRequestError('the title length is not right')
        paged["description"] = self.get_arg("description","")
        paged["keywords"] = self.get_arg("keywords","")
        paged["index"] = self.get_bool_arg("index",False)
        #todo get enterprise color
        paged["color"] = self.get_int_arg("color",2)

        #:todo 页面如果设为首页，需要查找吧其他页面改为False
        try:
            self.Mongopage.insert_one(paged)
            return SUCCESSFUL_RESPONSE
        except TypeError:
            return UnsupportMediaType
    def get_section(self):
        """
          {
              'pagecode':123513,    // 所属页面code
              'code':'navigation_bar',    // 版块编码
              'terminal':'wap',   // 版块所属终端
              'name':'导航栏',   // 版块名称
              'height':0, // 版块高度
              'floated':false,    // 版块是否浮动
              'horizontal':1, // 版块水平对齐，设置为浮动时有效，值：左0，中1，右2
              'vertical':2    // 版块垂直对齐,
              'order_index':0 //版块序号
              'layout_code':lr //版块布局
          }
          """
        sections = {}
        sections["code"] = self.get_arg("code","")
        if not sections["code"]:
            raise BadRequestError
        sections["page_code"] = self.get_arg("page_code","")
        if not sections["page_code"]:
            raise BadRequestError
        sections["terminal"] = self.get_arg("terminal","")
        sections["name"] = self.get_arg("name","")
        sections["height"] = self.get_int_arg("height",0)
        sections["floated"] = self.get_bool_arg("floated",False)
        sections["horizontal"] = self.get_int_arg("horizontal",1)
        sections["vertical"] = self.get_int_arg("vertical",1)
        sections["order_index"] = self.get_int_arg("order_index",0)
        sections["layout_code"] = self.get_arg("layout_code")
        try:
            self.Mongosection.insert_one(sections)
            return SUCCESSFUL_RESPONSE
        except TypeError:
            return UnsupportMediaType
    def get_layout(self):
        """
        {
            'code': 'code', // 布局编码
        'name': '左右结构' // 布局名称
        }
        """
        layout = self.Mongolayout.find({},{"_id":0})
        layoutslist = [x for x in layout]
        return {"status":1,"msg":"","layouts":layoutslist}
    def get_container(self):
        containers={}
        containers["code"] = self.get_arg("code","")
        containers["page_code"] = self.get_arg("page_code","")
        containers["layout_container_code"] = self.get_arg("layout_container_code","")
        try:
            self.Mongocontainer.insert_one(containers)
            return SUCCESSFUL_RESPONSE
        except TypeError:
            return UnsupportMediaType
    def get_layout_container(self):
        """
        {
    'code':'code', // 编码
    'module_limit':'5', // 模块数量限制
    'width_per':'30', // 宽度占页面宽度百分比
    'template_list':[12315,25423,89009324] // 可用模版Id列表
}
        :return:
        """
        layout_container = self.Mongolayout_container.find({},{"_id":0})
        return {"status":1,"msg":"","layouts":[x for x in layout_container]}
    def get_module(self):
        """
        
        :return:
        """
        modules = {}
        modules["page_section_code"] = self.get_arg("page_section_code","")
        modules["container_code"] = self.get_arg("container_code","")
        modules["data_source_id"] = self.get_int_arg("data_source_id")
        modules["data_source_order"] = self.get_int_arg("data_source_order")
        modules["order_index"] = self.get_int_arg("order_index")
        modules["template_id"] = self.get_int_arg("template_id")
        modules["template_settings"] = self.get_arg("template_settings")
        modules["template_datasource_rel"] = self.get_arg("template_datasource_rel")
        modules["out_link_rule"] = self.get_arg("out_link_rule")
        # module 子集
        module = {}
        module["code"] = self.get_arg("code")
        module["title"] = self.get_arg("title")
        module["link"] = self.get_arg("link")
        module["content"] = self.get_arg("content")
        module["image_url"] = self.get_arg("image_url")
        module["catalog"] = self.get_arg("catalog")
        module["biz_id"] =self.get_int_arg("biz_id")
        modules["module"] = module
        try:
            self.Mongomodule.insert_one(modules)
            return SUCCESSFUL_RESPONSE
        except TypeError:
            return UnsupportMediaType
    def get_data_source(self):
        data = self.Mongodata_source.find({},{"code":1,"name":1})
        return {"status":1,"msg":"","layouts":[x for x in data]}
    def get_data_order(self):
        """
         'orders': [{'code': 'name', 'name': '考试名称'},
  {'code': 'createtime', 'name': '考试创建时间'}]}

        :return: 
        """
        data_source_code = self.get_argument("data_source_code")
        data_order = self.Mongodata_source.find({"code":data_source_code})["orders"]
        return {"status":1,"msg":"","orders":data_order}
    def get_data_filter(self):
        data_source_code = self.get_argument("data_source_code")
        data_filter = self.Mongodata_source.find({"code": data_source_code})["filters"]
        return {"status": 1, "msg": "", "orders": data_filter}
    def get_module_template(self):

handlers = [
    (r"/(?P<res>[0-9a-zA-Z_]*)",PageCreate)
]

