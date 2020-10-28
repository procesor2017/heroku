from typing import Optional
from fastapi import FastAPI, File, UploadFile
from python.support import back_hello

app = FastAPI()

@app.get("/")
def read_root():
    return back_hello()