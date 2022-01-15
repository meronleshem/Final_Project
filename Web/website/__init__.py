from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "gnkdnvkggh"

    return app

