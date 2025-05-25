# How to deploy this app on cPanel

1. Log into cPanel.
2. Open "Setup Python App".
3. Click "Create Application".
   - Choose Python version (e.g., 3.9)
   - Set Application Root to `hello-flask`
   - Set Application URL to `/flask`
   - Set Entry Point to: `passenger_wsgi.py`
4. After creation, open Terminal or File Manager:
   - Upload files to the Application Root
   - Install requirements:
     ```bash
     source /home/USERNAME/virtualenv/hello-flask/3.9/bin/activate
     pip install -r requirements.txt
     ```
5. Visit your domain + URL path to test.
