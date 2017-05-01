from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.route("/ninja")
def ninja_page():
    return render_template("ninja_page.html")

@app.route("/ninja/<color>")
def color(color):
    return render_template("turtle_page.html", name=color)

app.run(debug=True)
