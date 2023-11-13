from flask import Flask
app = Flask(__name__)

import requests
from datetime import datetime

@app.route('/')
def hello_world():
    return f'Hello, World! {datetime.now()}'

@app.route('/ip')
def ip():
    url='https://httpbin.org/get'
    rs=requests.get(url)
    print('result:',url,rs.text)
    return rs.json()

