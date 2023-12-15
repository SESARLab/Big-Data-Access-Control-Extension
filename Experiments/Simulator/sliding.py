from node import Node
from nodeList import NodeList
from service import Service
import pandas
from node import Node

import itertools
NUMBER_OF_NODES = 10
NUMBER_OF_SERVICES = 5

if __name__ == "__main__":
  nodelist = NodeList()

  data = pandas.read_csv("cars.csv", sep=";")
  #data = pandas.read_csv("../inmates_enriched.csv")

  for i in range(0, NUMBER_OF_NODES):
    node = Node(i)
    for j in range(0, NUMBER_OF_SERVICES):
      service = Service(int(str(i) + str(j)))
      node.add_service(service)
    nodelist.add(node)

for i in range(0,len(nodelist.nodes)-1,1):
    name = nodelist.nodes[i]
    tag = nodelist.nodes[i+1]
    # print(f"{name} {tag}")
    combinazioni = itertools.product(name,tag)
    for combinazione in combinazioni:
      print(combinazione)


# combinazioni = itertools.product(*nodelist.nodes)


# # Stampare le combinazioni
# for combinazione in combinazioni:
#   nodelist = NodeList(combinazione)
#   data_logger.setNodeList(nodelist)

#   for idx,service in enumerate(combinazione):
#     node = Node(idx,service)
#     nodelist.add(node)

#   print(nodelist)
#   nodelist.run(data, data_logger)
#   del(nodelist)


# data_logger.store(f'stats_s{NUMBER_OF_SERVICES}n{NUMBER_OF_NODES}.csv')



