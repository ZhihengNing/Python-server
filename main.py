from flask import Flask

from algorithm import Algorithm
from application import analyse_app, BaseAlgorithm

BaseAlgorithm.__subclasses__().append(Algorithm)
app = Flask(__name__)
app.register_blueprint(blueprint=analyse_app)

if __name__ == "__main__":
    app.run()
