from flask import Flask, render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def name_page():
    return render_template("name_page.html")


@app.route('/process', methods=["POST"])
def process_page():
    print name
    name=request.form["name"]
    return redirect('/')


app.run(debug=True)
