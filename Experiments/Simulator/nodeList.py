import os
import uuid
from pathlib import Path
from typing import List

import configuration
from datalogger import DataLogger
from node import Node
from windowDecorator import WindowDecorator

os.path


class NodeList:
    def __init__(self, description=""):
        self.nodes: list[Node] = []
        self.description = description
        self.running = False
        self.id = "NODELIST"
        self.last_node: Node = None
        self._pointer = 0
        # self.WINDOW_SIZE = window_size

        self.winning_composition = []
        self.data_logger = None
        self.data = None

    def run(self, data, data_logger: DataLogger = None):
        self.running = True
        max = 0.0
        self.data_logger = data_logger
        self.data = data

        print(
            f"\033[92m n{configuration.NUMBER_OF_NODES}s{configuration.NUMBER_OF_SERVICES}w{configuration.WINDOW_SIZE}\033[0m")
        Path(f"Performance/N{configuration.NUMBER_OF_NODES}").mkdir(parents=True, exist_ok=True)

        # with ((open(f"Performance/N{configuration.NUMBER_OF_NODES}/results_{configuration.EXPERIMENT_ID}_w{configuration.WINDOW_SIZE}n{configuration.NUMBER_OF_NODES}s{configuration.NUMBER_OF_SERVICES}.txt", "w") as f)):
        while self.running:
            best_composition: List[Node]
            self.winning_composition: List[Node]
            best_composition, best_metrics = WindowDecorator(
                self.nodes[self._pointer:self._pointer + configuration.WINDOW_SIZE], data_logger
            ).run(data)

            total = 0.0
            if not self.is_last_window_frame():
                ###########WINDOW FRAME###########
                # taking only the first service of the best combination
                # print(best_composition[0], best_composition[0].get_current_service(), best_metric)
                configuration.WINDOW_ID = uuid.uuid4()

                combination = str(best_composition[0].get_current_service()) + ","

                data_logger.logAddCombination(configuration.NUMBER_OF_NODES, configuration.EXPERIMENT_ID,
                                              configuration.WINDOW_SIZE, configuration.NUMBER_OF_SERVICES, combination,
                                              best_metrics[0],
                                              best_composition[0].get_current_service().get_percentage())
            else:
                ############LAST WINDOW FRAME###########
                # take them all
                for node in best_composition:
                    print(node.get_current_service(), end=",")
                    combination = str(node.get_current_service()) + ","

                    data_logger.logAddCombination(configuration.NUMBER_OF_NODES, configuration.EXPERIMENT_ID,
                                                  configuration.WINDOW_SIZE, configuration.NUMBER_OF_SERVICES,
                                                  combination, node.metric, node.get_current_service().get_percentage())

            self.next()

    def next(self):
        # print("###########MOVING WINDOW###########")
        if self.is_last_window_frame():
            self.running = False
            self._pointer = 0

            # print("###########END###########")
            # print(self.winning_composition)
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
        return self._pointer == len(self.nodes) - configuration.WINDOW_SIZE

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return "".join(["s" + str(node.id) + str(node._pointer) for node in self.nodes])
