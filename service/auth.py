from util.redisConnect import redis

class Auth:
  def index(tocken):
    return redis.hget('login:', tocken)