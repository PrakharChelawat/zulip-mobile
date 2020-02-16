from flask import Flask, request, jsonify
from flask_cors import CORS
from news_scraper import scraper

app = Flask(__name__)
CORS(app)
API_URL = '/News_stock_prediction/api/v1/scrap_news'

@app.route('/summary',methods=['GET'])
def summary():
    company = ""
    sc = scraper(company)
    





if __name__ == '__main__':
    app.run(debug=False)