from app import create_app
from app.config.config_flask import Desenvolvimento

app = create_app(config_settings=Desenvolvimento())

if __name__ == "__main__":
    app.run()
