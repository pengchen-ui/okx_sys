from fastapi import FastAPI
from common.response import Response
app = FastAPI()


@app.get("/")
async def root():
    return Response.success("我是测试数据")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
