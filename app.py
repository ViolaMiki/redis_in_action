#!/usr/bin/env python
    
from flask import Flask
from flask import request

from service.auth import Auth

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/login', methods=['GET', 'POST'])
def login():
    controller = Auth()
    if request.method == 'POST':
        return Auth.index()
    else:
        return 'bbb'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
