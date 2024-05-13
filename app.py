from flask import Flask

from config.config_flask import Desenvolvimento

app: Flask = Flask(__name__)
app.config.from_object(Desenvolvimento())


if __name__ == "__main__":
    app.run()
