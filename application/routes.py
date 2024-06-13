from flask import request

from core import BaseResult, to_json_serializable, success
from . import analyse_app
from .analyse_server import AnalyseServer


@analyse_app.route('/', methods=['POST'])
def analyse() -> BaseResult:
    input_data = request.get_json()
    server = AnalyseServer.create()
    result = server.run(input_data)
    return result


@analyse_app.route('/test', methods=['GET'])
def test() -> str:
    print(to_json_serializable(success("111")))
    return "test success"
