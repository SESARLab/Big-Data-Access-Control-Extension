import numpy.random

class MatrixGenerator:
    weights = []

    def print_combinations(self, current_combination, depth, max_depth, services):
        if depth == max_depth:
            #print(*current_combination)
            self.weights.append(current_combination)
            return

        for i in range(services):
            self.print_combinations(current_combination + [round(numpy.random.uniform(0.8, 1), 3)], depth + 1,
                                    max_depth, services)
    def __init__(self):
        numpy.random.seed(50)
        from configuration import NUMBER_OF_NODES, NUMBER_OF_SERVICES
        self.NUMBER_OF_COMBINATION = NUMBER_OF_SERVICES ** NUMBER_OF_NODES
        # self.weights = numpy.random.uniform(0.8, 1, [self.NUMBER_OF_COMBINATION, NUMBER_OF_NODES])
        self.print_combinations([], 0, NUMBER_OF_NODES, NUMBER_OF_SERVICES)
    def get_weights(self):
        return self.weights
    def get_weight(self, combination, service):
        return self.weights.search_combination(combination)[0][service.parent.id]

#if __name__ == "__main__":
#    matrix = MatrixGenerator()
#    print(matrix)
#    print(matrix.get_weight(10, Service(0, parent=Node(0))))
