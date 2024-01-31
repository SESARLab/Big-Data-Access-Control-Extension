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
    e_nodes= 4
    configuration.NUMBER_OF_NODES = e_nodes
    for e_window in range(4,5):
        configuration.WINDOW_SIZE = e_window
        for e_servies in range(1, 15):
            configuration.NUMBER_OF_SERVICES = e_servies
            start_time = time.time()

            nodelist = NodeList(window_size=e_window)
            for i in range(0, configuration.NUMBER_OF_NODES):
                node = Node(i)

                for j in range(0, configuration.NUMBER_OF_SERVICES):
                    service = Service(int(f"{i}{j}"), parent=node)  # TODO: change this
                    node.add_service(service)
                nodelist.add(node)

            nodelist.run(data, data_logger)
            end_time = time.time()

            print(f"EXECUTION TIME w{e_window} n{e_nodes} s{e_servies}: {end_time - start_time}")
            # with open(f'event_newwindown_n{e_nodes}_w{e_window}.dat', 'a') as f_object:
            #     lista = [e_nodes,
            #     e_servies,
            #     e_window,
            #     end_time - start_time
            #     ]
            #     writer_object = writer(f_object, delimiter=' ')
            #     writer_object.writerow(lista)
            # f_object.close()

            # times.append(dict)

            # data_logger.store(f'stats_s{configuration.NUMBER_OF_SERVICES}n{configuration.NUMBER_OF_NODES}.csv')
