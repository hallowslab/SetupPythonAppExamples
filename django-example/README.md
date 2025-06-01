ASGI (for Django Channels, websockets, async features) is not supported in cPanel because it uses Passenger, which is WSGI-only.

# Django Example App for cPanel with Python Selector

This is a minimal Django web application demonstrating:
- WSGI compatibility with cPanel
- MySQL database integration
- Built-in user authentication (login/logout)
- Simple book listing
- File-based logging with filename and line number

---

## Environment variables

* DJANGO_DEBUG(Optional) 
* DJANGO_SECRET_KEY
* DJANGO_ADMIN_USERNAME
* DJANGO_ADMIN_EMAIL
* DJANGO_ADMIN_PASSWORD
* MYSQL_HOST(Optional)
* MYSQL_USER
* MYSQL_PASSWORD
* MYSQL_DB

---

## 🚀 Features

- WSGI-based Django app compatible with cPanel + CloudLinux Python Selector
- Uses Django’s built-in auth system
- Requires login to view book data
- Logs access and actions to `django_app.log`

---

## ⚙️ Setup Steps (cPanel)

1. **Create the Python App:**
   - Go to **Setup Python App**
   - Select Python version
   - Set `Application startup file`: `djangoexample/wsgi.py` or custom `passenger_wsgi.py`
   - Set `Application Entry point`: `application`
   - Set the working directory (where `manage.py` is)
   - Set [environment variables](#environment-variables)
   - Below "Configuration files" there is a field for files, add `requirements.txt`
   - Click Save and then click "pip install" (You might need to reload the page)


3. Run Django setup:
    * `python manage.py migrate`
    * `python manage.py createsuperuser`
