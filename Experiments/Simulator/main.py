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

    times = []
    for e_nodes in range(7, 10):
        configuration.NUMBER_OF_NODES = e_nodes
        for e_window in range(2, configuration.NUMBER_OF_NODES+1):
            configuration.WINDOW_SIZE = 2
            for e_servies in range(2, 10):
                configuration.NUMBER_OF_SERVICES = e_servies
                start_time = time.time()

                nodelist = NodeList(window_size=configuration.WINDOW_SIZE)
                for i in range(0, configuration.NUMBER_OF_NODES):
                    node = Node(i)

                    for j in range(0, configuration.NUMBER_OF_SERVICES):
                        service = Service(int(f"{i}{j}"), parent=node)  # TODO: change this
                        node.add_service(service)
                    nodelist.add(node)

                nodelist.run(data, data_logger)
                end_time = time.time()

                print(f"EXECUTION TIME {configuration.NUMBER_OF_NODES} {e_servies}: {end_time - start_time}")
                with open('event_window_2.csv', 'a') as f_object:
                    lista = [configuration.NUMBER_OF_NODES,
                    e_servies,
                    e_window,
                    end_time - start_time
                    ]
                    writer_object = writer(f_object)
                    writer_object.writerow(lista)
                f_object.close()

                times.append(dict)

                data_logger.store(f'stats_s{configuration.NUMBER_OF_SERVICES}n{configuration.NUMBER_OF_NODES}.csv')
