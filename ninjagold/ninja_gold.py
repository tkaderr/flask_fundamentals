from flask import Flask, render_template, request, redirect,session
import random
from time import strftime

app=Flask(__name__)
app.secret_key = "secret"
new_game=True


@app.route("/")
def home_page():
    global new_game
    if new_game:
        session["gold"]=0
        session["rand_coin"]=0
        session["log"]=["Hello, welcome"]
        new_game=False
    return render_template("game_page.html")

@app.route("/button", methods=["POST"])
def action_page():
    if request.form["action"]=="farm":
        session["rand_coin"]=random.randint(10,20)
        session["gold"]= session["gold"]+session["rand_coin"]
        session["log"].append("You earned "+str(session["rand_coin"])+" coins from the farm! "+str(strftime(" %Y-%m-%d %H:%M:%S")))
    elif request.form["action"]=="cave":
        session["rand_coin"]=random.randint(5,10)
        session["gold"]= session["gold"]+session["rand_coin"]
        session["log"].append("You earned "+str(session["rand_coin"])+" coins from the cave! "+str(strftime(" %Y-%m-%d %H:%M:%S")))
    elif request.form["action"]=="house":
        session["rand_coin"]=random.randint(2,5)
        session["gold"]= session["gold"]+session["rand_coin"]
        session["log"].append("You earned "+str(session["rand_coin"])+" coins from the house! "+str(strftime(" %Y-%m-%d %H:%M:%S")))
    elif request.form["action"]=="casino":
        session["rand_coin"]=random.randint(-50,50)
        session["gold"]= session["gold"]+session["rand_coin"]
        if session["rand_coin"]>=0:
            session["log"].append("You earned "+str(session["rand_coin"])+" coins from the casino! "+str(strftime(" %Y-%m-%d %H:%M:%S")))
        else:
            session["log"].append("You lost "+str(session["rand_coin"])+" coins from the casino! "+str(strftime(" %Y-%m-%d %H:%M:%S")))
    return redirect('/')
app.run(debug=True)
