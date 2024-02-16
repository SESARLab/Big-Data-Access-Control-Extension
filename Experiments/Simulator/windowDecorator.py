import copy

from combinationManager import CombinationManager
from node import Node


class WindowDecorator:
    def __init__(self, nodes: list[Node], data_logger):

        self.nodes = nodes
        self.running = True
        self.best_metric = 0.0
        self.best_metrics = []
        self.best_composition = []
        self.matrixW = CombinationManager(self.nodes).get_weights()
        self.data_logger = data_logger

    def run(self, data):
        while self.running:
            self.nodes[0].previous = self
            iteration_results = []
            iteration_metrics = []
            combination = "".join([str(node.get_current_service()) for node in self.nodes])
            for node in self.nodes:
                iter_result = node.run(data, self.matrixW[combination])
                self.data_logger.log(self.nodes, node.id, node._pointer, node.metric)
                # iteration_results.append(iter_result.result)
                iteration_metrics.append(iter_result.metric)

            avg_metric = sum(iteration_metrics) / len(iteration_metrics)
            if avg_metric > self.best_metric:
                self.best_composition = copy.deepcopy(self.nodes)
                self.best_metrics = copy.deepcopy(iteration_metrics)
                self.best_metric = avg_metric

            self.nodes[-1].next()

        return self.best_composition, self.best_metrics

    def next(self):
        self.running = False
