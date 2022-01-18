#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/1/18 20:08
from enum import Enum

dict_a = dict({'obj1': 1, 'obj2': 2})

enum_a = Enum('a', dict_a, module=__name__)

print(enum_a.obj1)
