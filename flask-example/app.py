import os
from string import ascii_letters as ALLOWED_CHARS
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return 'Hello, this is the home page!'

@app.route("/add-handled", methods=["POST"])
def add_handled():
    x = request.form.get("x", "")
    y = request.form.get("y", "")
    try:
        result = int(x) + int(y)
        return render_template("add.html", result=result, error=None)
    except ValueError:
        return render_template("add.html", result=None, error="Please provide valid integers for both x and y.")

@app.route("/add-unhandled", methods=["POST"])
def add_unhandled():
    x = request.form.get("x", "")
    y = request.form.get("y", "")
    result = int(x) + int(y)  # Will raise ValueError
    return render_template("add.html", result=result, error=None)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        assert all(c in ALLOWED_CHARS for c in name)
        assert all(c in ALLOWED_CHARS for c in email)
        assert all(c in ALLOWED_CHARS for c in message)

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
    return "pong"


