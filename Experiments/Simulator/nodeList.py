import itertools

from datalogger import DataLogger
from node import Node
import configuration
from windowDecorator import WindowDecorator

class NodeList:
    def __init__(self, description=""):
        self.nodes: list[Node] = []
        self.description = description
        self.running = False
        self.id = "NODELIST"
        self.last_node: Node = None
        self._pointer = 0
        self.WINDOW_SIZE = configuration.WINDOW_SIZE
        self.winning_composition = []
        self.data_logger = None
        self.data  = None

    def run(self, data, data_logger: DataLogger = None):
        self.running = True
        max = 0.0
        self.data_logger = data_logger
        self.data = data


        while self.running:
            best_composition: [Node]
            self.winning_composition: [Node]
            best_composition, best_metric = WindowDecorator(
                self.nodes[self._pointer:self._pointer + self.WINDOW_SIZE]).run(data)
            # data_logger.log(node.id, node._pointer, node.metrics[-1])
            total = 0.0
            if self.is_last_window_frame():
                print("###########LAST WINDOW FRAME###########")
                print("take them all")
                for node in best_composition:
                    print(node.get_current_service(), end=",")

            else:
                print("###########WINDOW FRAME###########")
                print("taking only the first service of the best combination")
                print(best_composition[0], best_composition[0].get_current_service(), best_metric)
            print("")
            self.next()





    def next(self):

        print("###########MOVING WINDOW###########")

        if self.is_last_window_frame():
            self.running = False
            self._pointer = 0

            print("###########END###########")
            print(self.winning_composition)

        else:
            self._pointer += 1
            self.nodes[self._pointer].previous = self

    def add(self, node):

        if len(self.nodes) > 0:
            node.previous = self.last_node
        else:
            node.previous = self

        self.nodes.append(node)
        self.last_node = node
        return self

    def remove(self, node):
        self.nodes.remove(node)
        return node

    def is_last_window_frame(self):
        return self._pointer == len(self.nodes) - self.WINDOW_SIZE

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return ",".join(["s" + str(node.id) + str(node._pointer) for node in self.nodes])
