from starlette.middleware.wsgi import WSGIMiddleware
from main import app as fastapi_app

# Convert FastAPI (ASGI) app to WSGI-compatible app
application = WSGIMiddleware(fastapi_app)
