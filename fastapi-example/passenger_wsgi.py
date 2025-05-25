from a2wsgi import ASGIMiddleware
from main import app as fastapi_app

application = ASGIMiddleware(fastapi_app)
