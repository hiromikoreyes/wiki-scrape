from flask import Flask, render_template

import scraper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('display.html')    