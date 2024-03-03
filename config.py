SMTP_KEY = "some_secret"
SMTP_USER = "user@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 465

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True


