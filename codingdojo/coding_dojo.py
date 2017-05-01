from flask import Flask, render_template, request,redirect, flash, session

app=Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def form_page():
    return render_template("form_page.html")

@app.route("/submit", methods=["POST"])
def form_submitted():
    session["location"]=request.form["location"]
    session["language"]=request.form["language"]
    if len(request.form["comment"])<5:
        flash("The comments are too short")
        return redirect('/')
    else:
        session["comment"]=request.form["comment"]
        flash("Name is sucessful")
        return render_template("form_submitted.html")
    if len(request.form["name"])<2:
        flash("The name is too short")
        return redirect('/')
    else:
        session["name"]=request.form["name"]
        flash("Name is sucessful")
        return render_template("form_submitted.html")
    return render_template("form_submitted.html")

app.run(debug=True)
