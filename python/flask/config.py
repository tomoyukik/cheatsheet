# https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/config.html

class Config(object):
    DEBUG = False
    TESTING = False
    CONFIG_FILE_PATH = 'common.cfg'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class TestConfig(Config):
    DEBUG = True
    TESTING = True
