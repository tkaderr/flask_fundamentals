from flask import Flask, render_template, request, redirect

app= Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/ninja')
def ninja_page():
    return render_template("ninja_page.html")

@app.route('/dojos/new')
def info_page():
    return render_template("form_page.html")

@app.route('/user', methods=["POST"])
def form_page():
    name=request.form["name"]
    email=request.form["email"]
    return redirect('/dojos/new')

app.run(debug=True)
