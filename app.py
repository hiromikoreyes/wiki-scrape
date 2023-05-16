from flask import Flask, render_template

import scraper

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html',content=scraper.body_string, title=scraper.title)    