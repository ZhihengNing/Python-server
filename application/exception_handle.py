from flask import jsonify

from core import failed, to_json_serializable
from . import analyse_app


@analyse_app.errorhandler(Exception)
def handle_error(e):
    error_res = to_json_serializable(failed(message=str(e)))
    print(error_res)
    return jsonify(error_res)
