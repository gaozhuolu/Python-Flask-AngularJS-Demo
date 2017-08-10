# project/config.py

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'my_precious'
    BCRYPT_LOG_ROUNDS = 13

    MONGODB_HOSTNAME = 'localhost:27017'
    MONGODB_USER = ""
    MONGODB_PWD = ""
