import itertools
import os
import uuid
from pathlib import Path
from typing import List

import configuration
import MatrixGenerator
from datalogger import DataLogger
from node import Node
from windowDecorator import WindowDecorator

os.path


class NodeList:
    def __init__(self, description=""):
        self.nodes: list[Node] = []

        self.description = description
        self.running = False
        self.last_node: Node = None
        self._pointer = 0

        self.winning_composition = []
        self.data_logger = None
        self.data = None

    def run(self, data, data_logger: DataLogger = None):
        MatrixGenerator.create_map(self.nodes)

        self.running = True
        max = 0.0
        self.data_logger = data_logger
        self.data = data

        print(
            f"\033[92m n{configuration.NUMBER_OF_NODES}s{configuration.NUMBER_OF_SERVICES}w{configuration.WINDOW_SIZE}\033[0m")


        while self.running:
            last_best_composition: List[Node]
            self.winning_composition: List[Node]
            window_start = self._pointer
            window_end = self._pointer + configuration.WINDOW_SIZE

            last_best_composition, last_best_metrics = WindowDecorator(

                self.nodes[window_start:window_end]
            ).run(data)

            if not self.is_last_window_frame():
                last_bast_service = last_best_composition[0].get_current_service()
                ###########WINDOW FRAME###########
                # taking only the first service of the best combination
                combination = str(last_bast_service)
                print(combination)

                data_logger.logAddCombination(
                    combination,
                    last_best_metrics[0],
                    last_bast_service.get_percentage()
                )

            else:
                ############LAST WINDOW FRAME###########
                # take them all
                for node in last_best_composition:
                    print(node.get_current_service(), end="")
                    combination = str(node.get_current_service())

                    data_logger.logAddCombination(
                        combination,
                        node.metric,
                        node.get_current_service().get_percentage()
                    )

            self.next()

    def next(self):
        ############MOVING WINDOW###########
        if self.is_last_window_frame():
            self.running = False
            self._pointer = 0
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

    def is_last_window_frame(self):
        return self._pointer == len(self.nodes) - configuration.WINDOW_SIZE

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return "".join(["s" + str(node.id) + str(node._pointer) for node in self.nodes])
