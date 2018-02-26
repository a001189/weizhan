#!/usr/local/bin python
# -*-coding:utf-8-*-
'''
author: ysj
time: 2017/9/21 下午3:48
desc:
'''
#!/usr/bin/env python
# -*-coding:utf-8-*-

from vmbsdk.errors import BadRequestError

DEGREE_VALUE_SCOPE = {"小学", "中学", "大学"}

class Field(object):
    def __init__(self, value, column_type,  max_length, min_length, not_null, value_scope=set()):
        self.value = value
        self.column_type = column_type
        self.max_length = max_length
        self.min_length = min_length
        self.not_null = not_null
        self.value_scope = value_scope

    def validate(self):
        if self.not_null:
            if self.value is None:
                raise BadRequestError
        elif self.value is None:
            self.value = self.column_type()
            return
        if not isinstance(self.value, self.column_type):
            raise BadRequestError
        if self.min_length:
            if len(self.value) < self.min_length:
                raise BadRequestError
        if self.max_length:
            if len(self.value) > self.max_length:
                raise BadRequestError
        if self.value_scope:
            if self.value not in self.value_scope:
                raise BadRequestError


class StringField(Field):
    def __init__(self, value, max_length=None, min_length=None, not_null=False, value_scope=set()):
        super(StringField, self).__init__(
            value,
            str,
            max_length,
            min_length,
            not_null,
            value_scope=value_scope)
        self.validate()


class IntegerField(Field):
    def __init__(self, value, not_null=False, value_scope=set()):
        super(IntegerField, self).__init__(
            value,
            (int, float), None, None,
            not_null=not_null,
            value_scope=value_scope)
        self.validate()


class NestedDocument(Field):
    def __init__(self, value, not_null=False):
        super(NestedDocument, self).__init__(
            value,
            dict, None, None,
            not_null=not_null
        )

class ArrayNestedDocument(Field):
    def __init__(self, value, not_null=False):
        super(ArrayNestedDocument, self).__init__(
            value,
            list, None, None,
            not_null=not_null
        )


class Teacher(object):
    """
    |name|含义|必填|类型|备注|
    | --- | --- | --- | --- | --- |
    | account_name | 用户名 | 是 | string | 来自数据库 |
    | name | 姓名 | 是 | string | 最大15个字（汉字、英文、标点都算一个字） |
    | position | 职位 | 是 | string | 最大长度25 |
    | introduction | 简介 | 是 | string | 最大长度800 |
    | degree | 学历 | 是 | string | 从下拉框选中 |
    | org_code | 组织机构编码 | 否 | string | 下拉框中选中 |
    | courses | 关联的课程 | 否 | [string, ] | 勾选 |
    | face | 头像uri | 否 | string | 调用上传头像接口获得图片uri |
    | motto | 座右铭 | 否 | string | 最大长度40 |
    | artistic_photo | 形象照uri | 否 | string |
    """
    __slots__ = ("account_name", "name", "position", "introduction", "degree", "org_code",
                 "org_name", "courses", "face", "motto", "artistic_photo")
    def __init__(self, **kwargs):
        for attr in self.__slots__:
            setattr(self, attr, kwargs.get(attr))
        self.validate_attr()

    def validate_attr(self):
        self.account_name = StringField(self.account_name, not_null=True)
        self.name = StringField(self.name, max_length=15, not_null=True)
        self.position = StringField(self.position, max_length=25, not_null=True)
        self.introduction = StringField(self.introduction, max_length=800, not_null=True)
        self.degree = StringField(self.degree, not_null=True, value_scope=DEGREE_VALUE_SCOPE)
        self.org_code = StringField(self.org_code, not_null=True)
        self.org_name = StringField(self.org_name, not_null=True)
        self.courses = ArrayNestedDocument(self.courses)
        self.face = StringField(self.face)
        self.motto = StringField(self.motto, max_length=40)
        self.artistic_photo = StringField(self.artistic_photo)

    def to_dict(self):
        d = {}
        for attr in self.__slots__:
            d[attr] = getattr(self, attr).value
        return d


class PartialTeacher(object):
    validate_mapping = {
        "name": {"field": StringField,
                 "kw": dict(max_length=15)},
        "position": {"field": StringField,
                     "kw": dict(max_length=25)},
        "introduction": {"field": StringField,
                         "kw": dict(max_length=800)},
        "degree": {"field": StringField,
                   "kw": dict(value_scope=DEGREE_VALUE_SCOPE)},
        "face": {"field": StringField,
                 "kw": dict()},
        "org_code": {"field": StringField,
                     "kw": dict()},
        "org_name": {"field": StringField,
                     "kw": dict()},
        "motto": {"field": StringField,
                  "kw": dict(max_length=40)},
        "artistic_photo": {"field": StringField,
                           "kw": dict()}
    }
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            field_cls = self.validate_mapping[k]["field"]
            kw = self.validate_mapping[k]["kw"]
            v = field_cls(v, **kw)
            setattr(self, k, v)

    def to_dict(self):
        d = {}
        for k in self.validate_mapping.keys():
            field_obj = getattr(self, k, None)
            if field_obj is not None:
                d[k] = field_obj.value
        return d



class OfflineCourse(object):
    __slots__ = ("name", "code", "teacher_ids")
    def __init__(self, **kwargs):
        for field in self.__slots__:
            setattr(self, field, kwargs.get(field))
        self.validate_attr()

    def validate_attr(self):
        pass

    def to_dict(self):
        pass


