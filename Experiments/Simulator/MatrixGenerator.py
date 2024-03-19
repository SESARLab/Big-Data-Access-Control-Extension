import itertools

import numpy.random

import configuration


def create_map(nodes):
    return ["".join(map(str, comb)) for comb in itertools.product(*nodes)]


class MatrixGenerator:
    weights = []

    def generate_weigths(self, current_combination, depth, max_depth, services):
        if depth == max_depth:
            self.weights.append(current_combination)
            return

        for i in range(services):
            self.generate_weigths(current_combination + [round(numpy.random.uniform(0.80, 1), 3)],
                                  depth + 1,
                                  max_depth, services)

    def __init__(self):
        self.weights = []
        numpy.random.seed(50 * configuration.EXPERIMENT_ID)
        self.NUMBER_OF_COMBINATION = configuration.NUMBER_OF_SERVICES ** configuration.NUMBER_OF_NODES
        self.generate_weigths([], 0, configuration.NUMBER_OF_NODES, configuration.NUMBER_OF_SERVICES)

    def get_weights(self):
         return self.weights

#    def get_weight(self, combination, service):
#        return self.weights.search_combination(combination)[0][service.parent.id]
