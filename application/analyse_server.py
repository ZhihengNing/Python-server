from flask import jsonify

from application.base_algorithm import BaseAlgorithm
from core import ApiException
from core.base_result import success
from core.util import DictToObject, to_json_serializable


class AnalyseServer:
    def __init__(self, algorithm: BaseAlgorithm):
        self.algorithm = algorithm

    @staticmethod
    def create(algorithm: BaseAlgorithm | None = None):
        if algorithm is None:
            subclass_list = BaseAlgorithm.__subclasses__()
            if len(subclass_list) == 0:
                raise ApiException("需创建一个BaseAlgorithm的子类")
            elif len(subclass_list) == 1:
                return AnalyseServer(subclass_list[0]())
            else:
                raise ApiException("BaseAlgorithm的子类过多")
        elif isinstance(algorithm, BaseAlgorithm):
            raise ApiException("需要实现实例化的对象")
        return AnalyseServer(algorithm)

    def run(self, input_data):
        param_names = self.algorithm.param_names
        if param_names is None:
            raise ApiException("params参数未配置")

        param_data = []
        for param in param_names:
            try:
                data = input_data.get(param)
                if isinstance(data, dict):
                    data = DictToObject(data)
                param_data.append(data)
            except Exception as e:
                raise e

        data = self.algorithm.implement(*param_data)
        return jsonify(to_json_serializable(success(data=data)))
