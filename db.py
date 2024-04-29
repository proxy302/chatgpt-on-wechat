#!/usr/bin/env python
# -*coding: utf-8 -*-

# Copyrighe 2024

# @author: jerrymoo


import ujson as json


mysql = None
redis = None

def db_cache(key, count=1, ttl=86400):
    """ 数据库缓存修饰器 """
    def db_cache_wrap(method):
        def wrapper(*args, **kwargs):
            key_name = "gpt302:%s" % key
            for i in range(count):
                key_name += ':%s' % args[i]
            data = redis.get(key_name)
            if not data:
                data = method(*args, **kwargs)
                if data:
                    redis.setex(key_name, ttl, json.dumps(data))
            else:
                data = json.loads(data)
            return data
        return wrapper
    return db_cache_wrap


def del_cache(key, *args):
    key_name = "gpt302:%s" % key
    for arg in args:
        key_name += ':%s' % arg
    redis.delete(key_name)


def cache1(ttl=86400):
    """ 新版数据库缓存接口
    功能：第一类cache：适用于数据极少变化的静态表，诸如：属性表 配置表 之类；
    参数：无参数，自动根据【函数名称】与【参数】的拼接作为Key进行Cache；
    """
    def db_cache_wrap(method):
        def wrapper(*args, **kwargs):
            key_name = "gpt302:%s" % method.__name__
            for parm in args:
                key_name += ':%s' % parm
            data = redis.get(key_name)
            if not data:
                data = method(*args, **kwargs)
                if data:
                    redis.setex(key_name, ttl, json.dumps(data))
            else:
                data = json.loads(data)
            return data
        return wrapper
    return db_cache_wrap
