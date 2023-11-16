from node import Node
from nodeList import NodeList
from service import Service
if __name__ == "__main__":

  p1 = {"region": "EU", "type": "web"}
  p2 = {"region": "EU", "type": "db"}
  p3 = {"region": "US", "type": "web"}
  p4 = {"region": "US", "type": "db"}

  px = {"region": "EU"}
  py = {"region": "US"}

  n1 = Node(px)
  n2 = Node(py)

  services =[Service(p1,"s1"), Service(p2,"s2"),  Service(p3,"s3"), Service(p4,"s4")]

  nodelist = NodeList()

  nodelist.add(n1)
  nodelist.add(n2)

  for node in nodelist.nodes:
    for service in services:
      if  node.match(service):
        print("Matched service {} ({}) to node {}".format(service.data,service.policy, node.policy))
      else:
        print("No match for service {} to node {}".format(service.data, node.policy))



