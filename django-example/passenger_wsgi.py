import sys
import os

# Add the project directory to sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Set the settings module (if not already set in wsgi.py)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoexample.settings")

# Import the app from Django's generated wsgi.py
from djangoexample.wsgi import application