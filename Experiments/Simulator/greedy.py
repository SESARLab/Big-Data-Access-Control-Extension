from node import Node
from nodeList import NodeList
from service import Service
import pandas
from node import Node
from datalogger import DataLogger
import itertools
import configuration

NUMBER_OF_NODES = configuration.NUMBER_OF_NODES
NUMBER_OF_SERVICES = configuration.NUMBER_OF_SERVICES
data = configuration.DATA
data_logger = DataLogger()

if __name__ == "__main__":
    nodelist = NodeList()
    for i in range(0, NUMBER_OF_NODES):
        node = Node(i)
        for j in range(0, NUMBER_OF_SERVICES):
            service = Service(int(str(i) + str(j).zfill(2)))
            print(f"Service {service.id}")
            node.addService(service)
        nodelist.add(node)
    bestPipeline = []
    for node in nodelist.nodes:
        bestPipeline.append(node.run(data).getBestService())

    instance = NodeList()
    for key, service in enumerate(bestPipeline):
        print(key, service)
        instance.add(Node(key, service))

    instance.run(data, data_logger)
    data_logger.store(f'stats_greedy_s{NUMBER_OF_SERVICES}n{NUMBER_OF_NODES}.csv')
