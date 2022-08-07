#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/5/23 20:30
import os
from string import Template

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse

upload = APIRouter()


@upload.get("/index_file")
def index_html2():
    # 这里的.在运行时是指FastAPI目录而不是APIRouter
    html_file = open(r".\Files\index.html", "r", encoding="UTF-8").read()
    return HTMLResponse(html_file)


@upload.get("/index")
def index_html():
    html_str = open(r".\Files\index.html", "r", encoding="UTF-8").read()
    html = Template(html_str)
    html = html.substitute({"HTTP": "http", "HOST": "127.0.0.1", "PORT": 8086})
    return HTMLResponse(html)


@upload.post("/uploader_1")
def upload_1(files: bytes = File(...)):
    return {"file_len": len(files)}


@upload.post("/uploader_2")
def upload_2(files: UploadFile = File(...)):
    return {"filename": files.filename}


@upload.get("/downloader")
def download_():
    return FileResponse("./Files/geek.7z", media_type="application/7z", filename="GG.7z")
