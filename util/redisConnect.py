from configparser import ConfigParser
from base import base

import redis

class DB():
  def __init__(self):
      self.__name = 'redis'
      self._db_config = self.__get_db_config()
      self.redis = self.connect(self._db_config)

  def __get_db_config(self):
      # 读取配置文件
      cfg = ConfigParser()
      cfg.read(base.flask_dir + '/redis.conf')

      # db配置参数
      db_config = {
          'host': cfg.get(self.__name, 'host'),
          'port': cfg.getint(self.__name, 'port'),
          'db': cfg.getint(self.__name, 'db')
      }
      return db_config

  def connect(self, config):
      return redis.Redis(host=config['host'], port=config['port'], db=config['db'])

db = DB()
redis = db.redis