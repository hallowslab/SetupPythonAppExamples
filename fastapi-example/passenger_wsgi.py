from a2wsgi import WSGIMiddleware
from main import app as fastapi_app

application = WSGIMiddleware(fastapi_app)
