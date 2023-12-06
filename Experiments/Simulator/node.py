import pandas


class Node(object):
    def __init__(self, id, service=None):
        self.id = id
        self.services = []
        self.results = []
        if service is not None:
            self.addService(service)

    def addService(self, service):
        self.services.append(service)

    def __repr__(self) -> str:
        return "Node n{}: {}\n".format(self.id, self.services)

    def run(self, data: pandas.DataFrame):
        print("Node n{} running".format(self.id))
        for service in self.services:
            service.run(data)
        return self

    def getOneService(self):
        return self.services.pop()

    def getServiceAt(self, index):
        return self.services[index]

    def getBestService(self):
        return min(self.services, key=lambda x: x.get_metric())

    def __iter__(self):
        return iter(self.services)
