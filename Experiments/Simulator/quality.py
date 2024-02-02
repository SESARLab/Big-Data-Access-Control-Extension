import time

import datalogger
from nodeList import NodeList
from service import Service
from csv import writer
from node import Node
import configuration


data = configuration.DATA
data_logger = datalogger.DataLogger()


def run_combination(combinazione):
    nodelist = NodeList(combinazione)
    for idx, service in enumerate(combinazione):
        node = Node(idx, service)
        nodelist.add(node)
    nodelist.run(data, data_logger)


if __name__ == "__main__":

    # e_nodes = 5
    # e_window = 5
    # e_servies = 5

    # configuration.NUMBER_OF_NODES = e_nodes
    # configuration.WINDOW_SIZE = e_window
    # configuration.NUMBER_OF_SERVICES = e_servies




    nodelist = NodeList()
    for i in range(0, configuration.NUMBER_OF_NODES):
        node = Node(i)

        for j in range(0, configuration.NUMBER_OF_SERVICES):
            service = Service(int(f"{i}{j}"), parent=node)  # TODO: change this
            node.add_service(service)
        nodelist.add(node)

    nodelist.run(data, data_logger)

    data_logger.store(f'stats_w{configuration.WINDOW_SIZE}s{configuration.NUMBER_OF_SERVICES}n{configuration.NUMBER_OF_NODES}.csv')