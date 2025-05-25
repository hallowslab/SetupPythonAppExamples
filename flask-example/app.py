from flask import Flask, render_template, request, redirect, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("All fields are required.", "error")
            return redirect("/flask-example")

        # Save submission to file (or send via SMTP)
        with open("submissions.txt", "a") as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

        flash("Thank you for contacting us!", "success")
        return redirect("/flask-example")

    return render_template("contact.html")
