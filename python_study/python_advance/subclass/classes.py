#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/1/23 10:22
from abc import ABC, abstractmethod


class B(ABC):

    @abstractmethod
    def add(self):
        pass


class Bsub(B):

    def add(self):
        print(1 + 2)


class A(ABC):

    @abstractmethod
    def __init__(self, b: B):
        self.b = b

    @abstractmethod
    def run_add(self):
        self.b.add()


class Asub(A):

    def __init__(self, b: Bsub):
        super(Asub, self).__init__(b)

    def run_add(self):
        super(Asub, self).run_add()


Asub(Bsub()).run_add()
