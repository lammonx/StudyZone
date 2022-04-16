#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/1/16 21:20
import os

import uvicorn
from fastapi import FastAPI
from Router import PrintRouter

app = FastAPI()
app.include_router(PrintRouter.print_, prefix='/print', tags=['打印服务'])

if __name__ == '__main__':
    # 启动方式1
    uvicorn.run('main:app', port=8086, reload=True, debug=True)
    # 启动方式2
    os.system('uvicorn main:app --port 8085  --reload')
