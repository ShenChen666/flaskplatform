from flaskp import app
from flask import render_template
from systeminfo import main

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = main.main()
    returnDict['title'] = 'Home'
    return render_template("index.html", **returnDict)
