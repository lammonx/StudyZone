#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/1/16 21:20

import uvicorn
from fastapi import FastAPI
from Router import PrintRouter

app = FastAPI()
app.include_router(PrintRouter.print_, prefix='/print', tags=['打印服务'])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8085, reload=True, debug=True)
