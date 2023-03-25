from flask import Flask
import scraper

app = Flask(__name__)



@app.route('/')
def home():
    return f'<h1>{scraper.title}</h1>'