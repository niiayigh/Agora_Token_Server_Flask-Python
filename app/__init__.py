import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # blueprint for agora
    from .agora import agora as agora_blueprint
    app.register_blueprint(agora_blueprint)

    # from .agora_rtm import agora_rtm as agora_rtm_blueprint
    # app.register_blueprint(agora_rtm_blueprint)

    return app
