#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/5/23 20:30
# depends on flask, werkzeug
from string import Template

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse

upload = APIRouter()


@upload.get("/index")
def index_html():
    html = Template("""
    <!DOCTYPE html>
    <html>
       <body>
         <div><a href="$HTTP://$HOST:$PORT/downloader" target="_self">下载文件</a></div>
         <br>
         <form action = "$HTTP://$HOST:$PORT/uploader_1" method = "POST"
            enctype = "multipart/form-data">
            <input type = "file" name = "files" multiple/>
            <input type = "submit"/>
         </form>
         <br>
         <form action = "$HTTP://$HOST:$PORT/uploader_2" method = "POST"
            enctype = "multipart/form-data">
            <input type = "file" name = "files" multiple/>
            <input type = "submit"/>
         </form>
       </body>
    </html>
    """)
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
