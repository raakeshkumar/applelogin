import os

from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/newlogin')
    def newlogin():
        return 'Hello, World!'

    from . import auth
    app.register_blueprint(auth.bp)

    return app
