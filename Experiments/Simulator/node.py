import pandas

import configuration
from service import Service


class Node(object):
    def __init__(self, id, service=None, previous=None):
        self.id = id
        self.services: [Service] = []
        self.result = None
        self.metric = None

        self._pointer = 0
        self.previous: Node = previous

        if service is not None:
            self.add_service(service)

    def add_service(self, service):
        self.services.append(service)

    def next(self):
        if self._pointer == len(self.services) - 1:
            self._pointer = 0
            if self.previous is not None:
                self.previous.next()
        else:
            self._pointer += 1

        return self

    def run(self, data: pandas.DataFrame, combination):
        configuration.increment_progress()
        output = self.services[self._pointer].run(data, combination[self.id])
        # self.result = ouput.result
        self.metric = output.metric
        # self.results.append(results.result)
        # self.metrics.append(results.metric)
        return self

    def get_current_service(self):
        return self.services[self._pointer]

    def get_service_at(self, index):
        return self.services[index]

    def __iter__(self):
        return iter(self.services)

    def __repr__(self) -> str:
        return "{}".format(self._pointer)

    # def __deepcopy__(self, memo):
    #     cls = self.__class__
    #     obj = cls.__new__(cls)
    #     memo[id(self)] = obj
    #     for k, v in self.__dict__.items():
    #         if k == ['previous']:
    #             v = dict()
    #         setattr(obj, k, deepcopy(v, memo))
    #         pass
    #     return obj
