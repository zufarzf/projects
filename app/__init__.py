# Ипортирование Flask
from flask import Flask
from config import config

# Ипортирование дополнения Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Иницилизация дополнений
db = SQLAlchemy()
migrate = Migrate()

from . import dbModels

# Фабричная функция
def create_app(config_name):
    
    # Иницилизация Flask
    app = Flask(__name__)
    # Указываем конфигурационный файл
    app.config.from_object(config[config_name])

    # Указываю на app для дополнений
    db.init_app(app)
    migrate.init_app(app, db)


    # Импортирую пакеты вложенных приложений
    from .admin import admin
    from .main import main
    from .errors import errors

    # Импортирую пакеты вложенных приложений
    app.register_blueprint(admin)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # Возвращаю приложение
    return app