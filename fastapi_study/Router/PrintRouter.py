#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/1/16 21:27

from fastapi import APIRouter, Query, Body

print_ = APIRouter()


@print_.post('/print_name0', name='打印字符0')
def print_name0(name: str = Body("AAA"), value: str = Body("CCC")):
    return {
            name: value,
            "2": "4"
    }


@print_.get('/print_name', name='打印字符')
def print_name(name: str = Query("AAA")):
    return name


@print_.get('/print_name2', name='打印字符')
def print_name2(name: str = Query("AAA")):
    return name + '打印字符2'


@print_.get('/print_num', name='打印数字')
def print_int(num: int = Query(123)):
    return num


@print_.get('/print_json', name='打印json')
def print_json():
    return {
            "牛逼一部": {
                    "xuw": "徐#伟",
                    "liym": "李#萌",
                    "wangxg": "王#纲",
                    "wangym": "王#萌",
                    "wangym1": "王#萌",
                    "wangym2": "王#萌",
                    "wangym3": "王#萌",
                    "wangym4": "王#萌",
                    "wangym11": "王#萌",
                    "wangym22": "王#萌",
                    "wangym33": "王#萌",
                    "wangym44": "王#萌",
            },
            "牛逼二部": {
                    "xuw": "徐#伟",
                    "liym": "李#萌",
                    "wangxg": "王#纲",
                    "wangym": "王#萌",
                    "wangym1": "王#萌",
                    "wangym2": "王#萌",
                    "wangym3": "王#萌",
                    "wangym4": "王#萌",
                    "wangym11": "王#萌",
                    "wangym22": "王#萌",
                    "wangym33": "王#萌",
                    "wangym44": "王#萌",
            },
            "牛逼三部": {
                    "xuw": "徐#伟",
                    "liym": "李#萌",
                    "wangxg": "王#纲",
                    "wangym": "王#萌",
                    "wangym1": "王#萌",
                    "wangym2": "王#萌",
                    "wangym3": "王#萌",
                    "wangym4": "王#萌",
                    "wangym11": "王#萌",
                    "wangym22": "王#萌",
                    "wangym33": "王#萌",
                    "wangym44": "王#萌",
            },
            "牛逼四部": {
                    "xuw": "徐#伟",
                    "liym": "李#萌",
                    "wangxg": "王#纲",
                    "wangym": "王#萌",
                    "wangym1": "王#萌",
                    "wangym2": "王#萌",
                    "wangym3": "王#萌",
                    "wangym4": "王#萌",
                    "wangym11": "王#萌",
                    "wangym22": "王#萌",
                    "wangym33": "王#萌",
                    "wangym44": "王#萌",
            }
    }
