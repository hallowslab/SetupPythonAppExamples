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

* MYSQL_HOST
* MYSQL_USER
* MYSQL_PASSWORD
* MYSQL_DB
* DJANGO_ADMIN_USERNAME
* DJANGO_ADMIN_EMAIL
* DJANGO_ADMIN_PASSWORD

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
   - Set `Application startup file`: `djangoexample/wsgi.py`
   - Set `Application Entry point`: `application`
   - Set the working directory (where `manage.py` is)
   - Set environment variables (optional), in your app environment: `DJANGO_SETTINGS_MODULE=djangoexample.settings`

2. **Install requirements:**
   Use the terminal or cPanel UI:
   - `pip install django mysqlclient`

3. Run Django setup:
    * `python manage.py migrate`
    * `python manage.py createsuperuser`

5. Configure database:
    - Edit settings.py with your cPanel MySQL credentials:
        ```DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your_db_name',
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
        ```