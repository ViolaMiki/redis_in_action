from flask import request

from util.help import create_tocken, set_cookie
from util.redisConnect import redis


class Auth:
    def index(self, token):
        result = {}

        # 从redis中获取登录信息
        name = redis.hget('login:', token)
        if name:
            result['name'] = str(name, encoding = "utf-8")
        else:
            result['error'] = 'token错误'
        return result

    def create(self):
        result = {}

        # 获取请求参数
        post_json = request.get_json()
        if 'user' in post_json and 'pwd' in post_json:
            result['token'] = create_tocken(post_json['user'])
            redis.hset('login:', result['token'], post_json['user'])
        return result

