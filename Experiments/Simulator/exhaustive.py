from node import Node
from nodeList import NodeList
from service import Service
import pandas
from node import Node
from datalogger import DataLogger
import itertools
import multiprocessing
import configuration
import concurrent.futures

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

    for i in range(0,NUMBER_OF_NODES):
        node = Node(i)
        for j in range(0, NUMBER_OF_SERVICES):
            service = Service(int(str(i) + str(j).zfill(2)))
            node.addService(service)
        nodelist.add(node)

    combinazioni = itertools.product(*nodelist.nodes)

#    for combinazione in combinazioni:
#        run_combination(combinazione)

    # Using a ThreadPoolExecutor for thread-based parallelism
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit each combination to the executor for printing
        executor.map(run_combination, combinazioni)

    data_logger.store(f'stats_s{NUMBER_OF_SERVICES}n{NUMBER_OF_NODES}.csv')
