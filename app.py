from flask import Flask, render_template, request, jsonify
import json
import scraper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/display/<query>')
def display(query):
    return render_template('display.html')

@app.route('/api-endpoint', methods=['POST'])
def getArticles():
    # print("getArticle() was called")
    data = json.loads(request.data)
    return jsonify(scraper.create_request(data['text']))