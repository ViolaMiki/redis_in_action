#!/usr/bin/env python
    
from flask import Flask, Response
from flask import request

from service.auth import Auth

import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/login', methods=['GET', 'POST'])
def login():
    controller = Auth()
    if request.method == 'POST':
        result = controller.create()
        if 'token' not in result:
            result['error'] = '请求参数错误'
            return json.dumps(result)
        else:
            response = Response()
            response.set_cookie('token', result['token'])
            response.set_data(json.dumps({'message':'登录成功'}))
            return response

    else:
        cookies = request.cookies
        if 'token' in cookies:
            result = controller.index(cookies['token'])
            return json.dumps(result)
        else:
            return json.dumps({'error':'请登陆'})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
