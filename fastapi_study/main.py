#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/1/16 21:20

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from Router import PrintRouter

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(PrintRouter.print_, prefix='/print', tags=['打印服务'])

if __name__ == '__main__':
    # 启动方式1
    import uvicorn
    uvicorn.run('main:app', port=8086, reload=True, debug=True)
    # 启动方式2
    # import os
    # os.system('uvicorn main:app --port 8085  --reload')
