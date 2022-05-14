#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/5/14 22:04


from fastapi import APIRouter, Query, Body

login = APIRouter()


@login.get("/get_user_id")
def get_user_id(user_name: str = Query("")):
    user_dict = {
            "牛逼一部": {
                    "wangxg": "王#纲",
                    "wangym": "王#萌"
            },
            "牛逼二部": {
                    "xuw": "徐#伟",
                    "liym": "李#萌"
            }
    }
    if user_name == "":
        return user_dict
    else:
        for dept, dept_users in user_dict.items():
            for userid, username in dept_users.items():
                if user_name == username:
                    return dict({dept: {userid: username}})
    raise RuntimeError("没找到该用户！")


@login.get("/get_env_list")
def get_env_list():
    return {
            "envs": ["st", "customer.st", "jyzl.st"]
    }


@login.get("/quick_login")
def quick_login(user_id: str = Query(""), env: str = Query("")):
    if user_id == "":
        raise RuntimeError("请输入正确id！")
    return {
            "data": f"{user_id}快捷登录{env}成功！！"
    }


@login.post("/common_login")
def common_login(user_id: str = Query(""), env: str = Query("")):
    if user_id == "":
        raise RuntimeError("请输入正确id！")
    return {
            "token": "niuniuniu"
    }


@login.post("/common_login_with_token")
def common_login_with_token():
    return {
            "data": f"常规登录成功！！"
    }
