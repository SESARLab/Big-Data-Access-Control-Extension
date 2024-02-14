import datalogger
import time
from nodeList import NodeList
from service import Service
from csv import writer
from node import Node
import configuration


data = configuration.DATA
data_logger = datalogger.DataLogger()

if __name__ == "__main__":
    MAX_NODES = 5
    MAX_SERVICES = 20

    configuration.increment_experiment_id()

    for s in range(5, MAX_SERVICES + 1,5):
        configuration.set_number_of_services(s)
        for n in range(2, MAX_NODES + 1):
            configuration.set_number_of_nodes(n)
            for w in range(1, n +1):
                start_time = time.time()
                configuration.set_window_size(w)

                nodelist = NodeList(description=f"n{configuration.NUMBER_OF_NODES}s{configuration.NUMBER_OF_SERVICES}w{configuration.WINDOW_SIZE}")
                for i in range(0, n):
                    node = Node(i)

                    for j in range(0, s):
                        service = Service(int(f"{i}{j}"), parent=node)  # TODO: change this
                        node.add_service(service)
                    nodelist.add(node)

                nodelist.run(data, data_logger)
                end_time = time.time()
                data_logger.logAddPercentage(end_time - start_time)

    data_logger.store(f'stats_w{configuration.WINDOW_SIZE}s{configuration.NUMBER_OF_SERVICES}n{configuration.NUMBER_OF_NODES}.csv')
    configuration.increment_experiment_id()
