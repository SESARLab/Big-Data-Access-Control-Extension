
from nodeList import NodeList
from service import Service

from node import Node
from datalogger import DataLogger
import configuration


NUMBER_OF_NODES = configuration.NUMBER_OF_NODES
NUMBER_OF_SERVICES = configuration.NUMBER_OF_SERVICES
data = configuration.DATA
data_logger = DataLogger()


def run_combination(combinazione):
    nodelist = NodeList(combinazione)
    for idx, service in enumerate(combinazione):
        node = Node(idx, service)
        nodelist.add(node)
    nodelist.run(data, data_logger)


if __name__ == "__main__":
    nodelist = NodeList()

    for i in range(0, NUMBER_OF_NODES):
        node = Node(i)
        for j in range(0, NUMBER_OF_SERVICES):
            service = Service(int(f"{i}{j}"))  # TODO: change this
            node.add_service(service)
        nodelist.add(node)
    print(nodelist)

    nodelist.run(data, data_logger)
    # WINDOW_SIZE = 1

    # for i in range(0,NUMBER_OF_NODES):
    #     if(i+WINDOW_SIZE > NUMBER_OF_NODES):
    #         break
    #     combinazioni = itertools.product(*nodelist.nodes[i:i+WINDOW_SIZE])
    #
    #     for combinazione in combinazioni:
    #         run_combination(combinazione)

    data_logger.store(f'stats_s{NUMBER_OF_SERVICES}n{NUMBER_OF_NODES}.csv')
