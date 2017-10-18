from flask import request

from util.help import create_tocken, set_cookie
from util.redis_connect import redis

import time


class Auth:

    # 登录用户信息更新
    def update_token(self, token, user, item=None):
        timestamp = time.time()
        redis.hset('login:', token, user)
        redis.zadd('recent:', token, timestamp)

    # 获取登录用户信息
    def index(self, token):
        result = {}

        # 从redis中获取登录信息
        name = redis.hget('login:', token)
        if name:
            result['name'] = str(name, encoding = "utf-8")

            # 通过验证后更新token信息
            self.update_token(token, name)
        else:
            result['error'] = 'token错误'
        return result

    # 创建token
    def create(self):
        result = {}

        # 获取请求参数
        post_json = request.get_json()
        if 'user' in post_json and 'pwd' in post_json:
            result['token'] = create_tocken(post_json['user'])
            redis.hset('login:', result['token'], post_json['user'])
        return result

