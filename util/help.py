from http import cookies

import hashlib, time, datetime, random


def create_tocken(user):
    token = hashlib.md5()
    token.update((user + str(time.time())).encode('UTF-8'))
    return token.hexdigest()

def set_cookie(key, value):
    expiration = datetime.datetime.now() + datetime.timedelta(days=30)
    cookie = cookies.SimpleCookie()
    cookie["session"] = random.randint(1, 1000000000)
    cookie["session"]["domain"] = "localhost"
    cookie["session"]["path"] = "/"
    cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
    cookie[key] = value
    print(cookie.output())