from app import create_app
from config import config_type
import os

app = create_app(os.environ.get("FLASK_ENV") or "default")

if __name__ == "__main__":
    app.run()