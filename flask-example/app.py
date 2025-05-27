import os
import logging
from string import ascii_letters as ALLOWED_CHARS
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)


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

@app.route("/")
def home():
    return 'Hello, this is the home page!'

@app.route("/add-handled", methods=["GET", "POST"])
def add_handled():
    if request.method == "POST":
        x = request.form.get("x", "")
        y = request.form.get("y", "")
        logger.info(f"Handled Add: Received x={x}, y={y}")
        try:
            result = int(x) + int(y)
            logger.info(f"Handled Add: Result = {result}")
            return render_template("add.html", result=result, error=None)
        except ValueError as e:
            logger.warning(f"Handled Add: Invalid input x={x}, y={y} — {e}")
            return render_template("add.html", result=None, error="Please provide valid integers.")
    return render_template("add.html", result=None, error=None)

@app.route("/add-unhandled", methods=["GET", "POST"])
def add_unhandled():
    if request.method == "POST":
        x = request.form.get("x", "")
        y = request.form.get("y", "")
        logger.info(f"Unhandled Add: Received x={x}, y={y}")
        result = int(x) + int(y)
        logger.info(f"Unhandled Add: Result = {result}")
        return render_template("add.html", result=result, error=None)
    return render_template("add.html", result=None, error=None)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        try:
            assert all(c in ALLOWED_CHARS for c in name)
            assert all(c in ALLOWED_CHARS for c in email)
            assert all(c in ALLOWED_CHARS for c in message)
        except AssertionError:
            flash("Invalid characters.", "error")

        if not name or not email or not message:
            flash("All fields are required.", "error")
            return redirect("/flask-example")

        # Save submission to file (or send via SMTP)
        with open("submissions.txt", "a") as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

        flash("Thank you for contacting us!", "success")
        return redirect("/flask-example")

    return render_template("contact.html")

@app.route("/ping")
def ping():
    logger.info("PONG")
    return "pong"


