from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ip')
def hello_wo2rld():
    url='https://httpbin.org/get'
    rs=requests.get(url)
    return rs.json()

