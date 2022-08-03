class Config:
    SECRET_KEY = '9615e623d2b9d92ec6802887503bc7385e0f4b54a4cee313b038d9018fb4'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = '127.0.0.1:5000'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site_db.db'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site_db_prod.db'


config = {
            "default":DevConfig,
            "development":DevConfig,
            "testing":TestingConfig,
            "production":ProdConfig
        }