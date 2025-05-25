from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    # return {"message": "pong"}
    return {"message": f"FastAPI, version: {app.version}"}

@app.get("/ping")
def ping():
    # return {"message": "pong"}
    return {"message": "pong"}

@app.get("/hello")
def hello(name: str = "world"):
    # return {"message": f"Hello, {name}!"}
    return {"message": f"Hello, {name}!"}
