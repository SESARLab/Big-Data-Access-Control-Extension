import itertools

from MatrixGenerator import MatrixGenerator
import configuration

class CombinationManager:
    def __init__(self, nodes):
        self.nodes = nodes
        self.services = []
        self.combinations = []
        matrix = MatrixGenerator()
        combination = ["".join(map(str, comb)) for comb in itertools.product(*self.nodes)]
        self.combinations = dict(zip(combination, matrix.get_weights()))
        configuration.set_total_combinations(len(self.combinations))


    def get_combination(self):
        for node in self.nodes:
            self.services.append(node.get_current_service())

        return self.services

    def __repr__(self):
        return "{}".format(self.services)

    def __str__(self):
        return "{}".format(self.services)

    def get_weights(self):
        return self.combinations


    def search_combination(self,combination):
        return [val for key, val in self.combinations.items() if combination in key]


if __name__ == "__main__":
    from node import Node
    from service import Service

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.add_service(Service(11))
    node1.add_service(Service(12))
    node1.add_service(Service(13))
    node1.add_service(Service(14))
    node1.add_service(Service(15))

    node2.add_service(Service(21))
    node2.add_service(Service(22))
    node2.add_service(Service(23))
    node2.add_service(Service(24))
    node2.add_service(Service(25))

    node3.add_service(Service(31))
    node3.add_service(Service(32))
    node3.add_service(Service(33))
    node3.add_service(Service(34))
    node3.add_service(Service(35))

    node4.add_service(Service(41))
    node4.add_service(Service(42))
    node4.add_service(Service(43))
    node4.add_service(Service(44))
    node4.add_service(Service(45))

    node5.add_service(Service(51))
    node5.add_service(Service(52))
    node5.add_service(Service(53))
    node5.add_service(Service(54))
    node5.add_service(Service(55))

    nodes = [node1, node2, node3, node4, node5]

    combination = CombinationManager(nodes)
    #print(combination.get_weights())
    print(combination.search_combination("s11s22"))

