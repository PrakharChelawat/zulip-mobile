from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from news_scraper import scraper
import json
app=Flask(__name__)
CORS(app)
@app.route('/',methods=['POST'])
def scraping():
    company = ''
    sc = scraper(company)
    d = sc.pretty_print()
    return make_response(d)

if __name__ == '__main__':
    app.run(debug=False)