from flask import Flask, render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def name_page():
    return render_template("name_page.html")
