import numpy as np

from is3app import BaseAlgorithm


class Algorithm(BaseAlgorithm):
    def implement(self, a, b):
        return {
            'a': np.array([1, 3]),
            'b': {
                "2": {1, 2, 3},
                "c": a / sum(b.c)
            }
        }


