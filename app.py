from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

# Constants
NEWS_API_URL = 'https://api.marketaux.com/v1/news/all'
API_TOKEN = '8tHNPlA4icrWvJOOPAYKGmp1CG6Vdwj8XuIVmlLt'

# Fetch news data
def fetch_news():
    response = requests.get(
        NEWS_API_URL,
        params={
            'symbols': 'TSLA,AMZN,MSFT',
            'filter_entities': 'true',
            'language': 'en',
            'api_token': API_TOKEN
        }
    )
    return response.json().get('data', [])

@app.route('/')
def index():
    news_data = fetch_news()
    return render_template('index.html', news_data=news_data)

@app.route('/read/<int:index>')
def read(index):
    news_data = fetch_news()
    if index < 0 or index >= len(news_data):
        return redirect('/')
    news_item = news_data[index]
    return render_template('news_item.html', news_item=news_item, index=index, total=len(news_data))

if __name__ == '__main__':
    app.run(debug=True)
