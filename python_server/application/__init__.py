from flask import Blueprint

from .base_algorithm import BaseAlgorithm

analyse_app = Blueprint('analyse', __name__, url_prefix='/analyse')

# 要在这个地方先import才能用
from .routes import *
from .exception_handle import *