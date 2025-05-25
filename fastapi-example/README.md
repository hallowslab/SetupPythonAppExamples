# FastAPI on cPanel – Minimal API Example

This is a lightweight FastAPI project designed for shared hosting on **cPanel with CloudLinux Python Selector**. It uses WSGI middleware to adapt FastAPI (normally ASGI) to work in cPanel’s environment.

---

## ⚙️ Features

- `/`: Returns `{"message": f"FastAPI, version: {app.version}"}`
- `/ping`: Returns `{ "message": "pong" }`
- `/hello?name=YourName`: Returns personalized JSON response

---

## 🧱 Project Structure

fastapi-example/
├── main.py
├── passenger_wsgi.py
├── requirements.txt

--

## 🚀 Deployment Steps (via cPanel)

### 1. Log into cPanel and Open **Setup Python App**

Located in the "Software" section.

### 2. Create a New Python App

- **Python version**: `3.9` or higher
- **Application root**: `public_html/fastapi-example`
- **Application URL**: `/fastapi-example` (or anything you like)
- **Application startup file**: `passenger_wsgi.py`
- **Application entry point**: `application`
- **Passenger log file**: `public_html/fastapi-example/passenger.log` The path of the logfile for passenger
- Click **Create**

---

### 3. Upload the Files

Upload the following to your `~/fastapi-example/` directory:

- `main.py`
- `passenger_wsgi.py`
- `requirements.txt`

You can use **File Manager** or **FTP/SFTP**.

---

### 4. Install Dependencies

### If Terminal is enabled:

Use **Terminal** (or SSH) to activate your virtualenv and install:

```bash
source ~/virtualenv/fastapi-example/3.9/bin/activate
cd ~/fastapi-example
pip install -r requirements.txt
```

### If terminal is disabled:

Edit the python application in the Setup Python App plugin

- Below "Configuration files" there is a field for files, add `requirements.txt`
- Click Save and then click "pip install" (You might need to reload the page)


