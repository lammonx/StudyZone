#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/1/16 21:27

from fastapi import APIRouter, Query

print_ = APIRouter()


@print_.get('/print_name', name='打印字符')
def print_name(name: str = Query(..., alias="字符")):
    return name


@print_.get('/print_int', name='打印数字')
def print_int(_int: int = Query(..., alias="数字")):
    return _int
