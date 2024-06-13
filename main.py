from flask import Flask

from algorithm import Algorithm
from application import analyse_app, BaseAlgorithm
from core import to_json_serializable, success

BaseAlgorithm.__subclasses__().append(Algorithm)
app = Flask(__name__)
app.register_blueprint(blueprint=analyse_app)

if __name__ == "__main__":
    app.run()
