from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    # return {"message": "pong"}
    return JSONResponse({"message": f"FastAPI, version: {app.version}"},200)

@app.get("/ping")
def ping():
    # return {"message": "pong"}
    return JSONResponse({"message": "pong"},200)

@app.get("/hello")
def hello(name: str = "world"):
    # return {"message": f"Hello, {name}!"}
    return JSONResponse({"message": f"Hello, {name}!"})
