from flask import Flask, render_template, request

import scraper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('display.html')

@app.route('/api/endpoint', methods=["GET", "POST"])
def getArticles():
    if request.method == "POST":
        print("A post request has been sent by a user")
