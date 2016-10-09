# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("UTF-8")
from requests import get
from retrying import retry


@retry(stop_max_attempt_number=2)
def getProxy(path='qyxx', **kwargs):
    '''
    获取代理的接口
    :param path: url路径
    :param kwargs: area=spider_name 必须存在,last=last_proxy default == None ,type=获取代理的类型，default == None
    :return:
    '''
    url = "http://c4node30:42273/%s" % path
    assert kwargs.get('area') != None, "spider name error......"
    if 'last' not in kwargs:
        kwargs['last'] = 'None'
    if 'type' not in kwargs:
        kwargs['type'] = 'None'
    params = kwargs
    proxy = get(url, params=params).text.strip()
    return proxy

