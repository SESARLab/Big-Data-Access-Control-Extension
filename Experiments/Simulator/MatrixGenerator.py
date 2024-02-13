import numpy.random
import configuration
class MatrixGenerator:
    weights = []

    def print_combinations(self, current_combination, depth, max_depth, services):
        if depth == max_depth:
            self.weights.append(current_combination)
            return

        for i in range(services):
            self.print_combinations(current_combination + [round(numpy.random.uniform(0.95, 1), 3)], depth + 1,
                                    max_depth, services)
    def __init__(self):
        self.weights = []
        numpy.random.seed(50*configuration.EXPERIMENT_ID)

        self.NUMBER_OF_COMBINATION = configuration.NUMBER_OF_SERVICES ** configuration.NUMBER_OF_NODES
        # self.weights = numpy.random.uniform(0.8, 1, [self.NUMBER_OF_COMBINATION, NUMBER_OF_NODES])
        self.print_combinations([], 0, configuration.NUMBER_OF_NODES, configuration.NUMBER_OF_SERVICES)
    def get_weights(self):
        return self.weights
    def get_weight(self, combination, service):
        return self.weights.search_combination(combination)[0][service.parent.id]