from flask import Flask, redirect, request, render_template, session, flash
import re

app=Flask(__name__)
app.secret_key=("secret_key")

FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
LAST_NAME_REGEX =re.compile(r'^[a-zA-Z]*$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def registration_page():
    return render_template("registration.html")

@app.route('/users', methods=["POST"])
def submitted_data():
    first_name=str(request.form["first_name"])
    last_name=str(request.form["last_name"])
    email_name=str(request.form["email_name"])
    password=str(request.form["password"])
    confirm_password=str(request.form["confirm_password"])

    if len(first_name)<2 or not FIRST_NAME_REGEX.match(first_name) or str.isalpha(first_name) != True:
        flash("The first name is too short and invalid letters")
        return redirect('/')
    else:
        session["first_name"]=first_name
    if len(last_name)<2 or not LAST_NAME_REGEX.match(first_name) or str.isalpha(last_name)!=True:
        flash("The last name is too short and invalid letters")
        return redirect('/')
    else:
        session["last_name"]=last_name
    if len(email_name)<2 or not EMAIL_REGEX.match(email_name):
        flash("The email is invalid")
        return redirect('/')
    else:
        session["email_name"]=email_name
    if len(password)<1:
        flash("The password is too short")
        return redirect('/')
    else:
        session["password"]=password
    if len(confirm_password)<2 or confirm_password!= session["password"]:
        flash("The passwords do not match")
        return redirect('/')
    return render_template("submitted_form.html")

app.run(debug=True)
