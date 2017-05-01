from flask import Flask, render_template, request, redirect,session

app=Flask(__name__)
app.secret_key = "secret"

first_visit=True


@app.route('/')
def home_page():
    global first_visit
    if first_visit:
        session["counter"]=1
        first_visit=False
    else:
        session["counter"]+=1
    return render_template("home_page.html")

@app.route('/button', methods=["POST"])
def counter_page():
    if request.form["action"]=="add2":
        session["counter"]+=1
    elif request.form["action"]=="reset":
        first_visit=True
        session["counter"]=0
    return redirect ('/')


app.run(debug=True)
