# Flask Contact Form – cPanel Deployment Guide

This is a simple **Flask contact form app** designed to run on shared hosting via **cPanel + CloudLinux's Python Selector**. It demonstrates:


- How to setup a python app
- How to install dependencies

---

## 🚀 How to Deploy on cPanel

### 1. Log into cPanel

### 2. Open **Setup Python App**
Under the "Software" section in cPanel, click **Setup Python App**.

### 3. Create a New Python Application
- **Python version**: Select 3.9+ (e.g., 3.9 or 3.11 if available)
- **Application root**: `public_html/flask-example`
- **Application URL**: `flask-example` (or your desired path)
- **Application startup file**: `passenger_wsgi.py`
- **Application Entry point**: `application` The Object to be called which we define in `passenger_wsgi.py`
- **Passenger log file**: `public_html/flask-example/passenger.log` The path of the logfile for passenger
- Click **Create**

---

## 📁 4. Upload the App Files

Upload the following to your app's **Application root directory** (e.g., `~/flask-example/`):

- `app.py`
- `passenger_wsgi.py`
- `requirements.txt`
- A `templates/` folder containing `contact.html`

You can use **File Manager** or connect via **FTP/SFTP**.

---

## 📦 5. Install Dependencies

### If Terminal is enabled:

Go to **Terminal** (or SSH), and activate your Python virtual environment:

```bash
source ~/virtualenv/hello-flask/3.9/bin/activate
cd ~/hello-flask
pip install -r requirements.txt
```


### If terminal is disabled:

Edit the python application in the Setup Python App plugin

- Below "Configuration files" there is a field for files, add `requirements.txt`
- Click Save and then click "pip install" (You might need to reload the page)