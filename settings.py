#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : Sam Zhou
date   : 2017/9/13 10:57
role   : Version Update
'''
import os

from vmbsdk.constants.consts import const

ROOT_DIR = os.path.dirname(__file__)

log_path = os.path.join(ROOT_DIR, 'logs', 'app.log')

template_path = os.path.join(ROOT_DIR, "templates")
static_path = os.path.join(ROOT_DIR, "static")

debug = True
xsrf_cookies = False

api_service_url = 'cs-api.vmceshi.com'
service_sso2_domain = 'cs-sso2.vmceshi.com'
service_sso2_port = '80'

ht_domain = '192.168.1.157:8000'

index_url = 'http://' + ht_domain + '/'

sso2_call_back = 'http://' + ht_domain + '/sso_callback/'

cookie_secret = '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo='
expire_seconds = 365 * 24 * 60 * 60

bucket = 'km-test'


DEFAULT_DB_DBHOST = '192.168.1.12'
DEFAULT_DB_DBPORT = '3306'
DEFAULT_DB_DBUSER = 'vmobel'
DEFAULT_DB_DBPWD = 'a7NVZSdp'
DEFAULT_DB_DBNAME = 'vmobel'

READONLY_DB_DBHOST = '192.168.1.13'
READONLY_DB_DBPORT = '3306'
READONLY_DB_DBUSER = 'readonly'
READONLY_DB_DBPWD = 'vmobel2016'
READONLY_DB_DBNAME = 'vmobel'

DEFAULT_MQ_ADDR = '192.168.1.67'
DEFAULT_MQ_PORT = 56720
DEFAULT_MQ_VHOST = '/'
DEFAULT_MQ_USER = 'yz'
DEFAULT_MQ_PWD = 'vuz84B2IkbEtXWF'

DEFAULT_REDIS_HOST = '192.168.1.35'
DEFAULT_REDIS_PORT = 6379
DEFAULT_REDIS_DB = 11
DEFAULT_REDIS_AUTH = True
DEFAULT_REDIS_CHARSET = 'utf-8'
DEFAULT_REDIS_PASSWORD = 'Vmobel135791'

MONGO_DB = 'weizhan'
MONGO_HOST = 'localhost'
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'Vmobel2016'
MONGO_PORT = 27017

settings = dict(
    template_path=template_path,
    static_path=static_path,
    debug=debug,
    xsrf_cookies=xsrf_cookies,
    cookie_secret=cookie_secret,
    expire_seconds=expire_seconds,
    databases={
        const.DEFAULT_DB_KEY: {
            const.DBHOST_KEY: DEFAULT_DB_DBHOST,
            const.DBPORT_KEY: DEFAULT_DB_DBPORT,
            const.DBUSER_KEY: DEFAULT_DB_DBUSER,
            const.DBPWD_KEY: DEFAULT_DB_DBPWD,
            const.DBNAME_KEY: DEFAULT_DB_DBNAME,
        },
        const.READONLY_DB_KEY: {
            const.DBHOST_KEY: READONLY_DB_DBHOST,
            const.DBPORT_KEY: READONLY_DB_DBPORT,
            const.DBUSER_KEY: READONLY_DB_DBUSER,
            const.DBPWD_KEY: READONLY_DB_DBPWD,
            const.DBNAME_KEY: READONLY_DB_DBNAME,
        }
    },
    mqs={
        const.DEFAULT_MQ_KEY: {
            const.MQ_ADDR: DEFAULT_MQ_ADDR,
            const.MQ_PORT: DEFAULT_MQ_PORT,
            const.MQ_VHOST: DEFAULT_MQ_VHOST,
            const.MQ_USER: DEFAULT_MQ_USER,
            const.MQ_PWD: DEFAULT_MQ_PWD,
        }
    },
    redises={
        const.DEFAULT_RD_KEY: {
            const.RD_HOST_KEY: DEFAULT_REDIS_HOST,
            const.RD_PORT_KEY: DEFAULT_REDIS_PORT,
            const.RD_DB_KEY: DEFAULT_REDIS_DB,
            const.RD_AUTH_KEY: DEFAULT_REDIS_AUTH,
            const.RD_CHARSET_KEY: DEFAULT_REDIS_CHARSET,
            const.RD_PASSWORD_KEY: DEFAULT_REDIS_PASSWORD
        }
    },
    mongodbs={
            'db': MONGO_DB,
            'host': MONGO_HOST,
            'username': MONGO_USERNAME,
            'password': MONGO_PASSWORD,
            'port': MONGO_PORT
        },
    app_name='weizhan',
    log_path=log_path,
    api_service_url=api_service_url,
    service_sso2_domain=service_sso2_domain,
    service_sso2_port=service_sso2_port,
    bucket=bucket,
    sso2_call_back=sso2_call_back,
    index_url=index_url,
)