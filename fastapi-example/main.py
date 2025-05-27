import logging
from fastapi import FastAPI

app = FastAPI()

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detail
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Logs to the specified file
        logging.StreamHandler()          # If stream is not specified, sys.stderr is used (useful in cPanel logs)
    ]
)

logger = logging.getLogger(__name__)

@app.get("/")
def home():
    logger.info(f"Request for /, displaying version {app.version}")
    return {"message": f"FastAPI, version: {app.version}"}

@app.get("/ping")
def ping():
    logger.info(f"Request for /ping, replying with pong!")
    return {"message": "pong!"}

@app.get("/hello")
def hello(name: str = "world"):
    logger.info(f"request at /hello from {name}")
    return {"message": f"Hello, {name}!"}
