from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    print(f"Request for /, displaying version {app.version}")
    return {"message": f"FastAPI, version: {app.version}"}

@app.get("/ping")
def ping():
    print(f"Request for /ping, replying with pong!")
    return {"message": "pong!"}

@app.get("/hello")
def hello(name: str = "world"):
    print(f"request at /hello from {name}")
    return {"message": f"Hello, {name}!"}

@app.post("/add")
async def calc(request: Request):
    data = await request.json()
    print(f"request at /add for {data}")
    try:
        x = data.get("x", None)
        y = data.get("y", None)
        if x is None or y is None:
            raise ValueError(f"Missing values: {x}:{y}")
        res = x+y
        return {"message": res}
    except Exception as e:
        print(f"/add failed because: {e}")
        return {"message": f"Error: {e}"}
    
@app.post("/unadd")
async def bcalc(request: Request):
    data = await request.json()
    x = data.get("x", None)
    y = data.get("y", None)
    print(f"request at /add for {x}+{y}")
    return {"message": x+y}