from typing import Self

import pandas

from metrics import jsh


class Service:
    # def __init__(self, id, profile: ServiceProfile = PregeneratedProfiles.GOOD, parent=None):
    def __init__(self, id, parent=None):
        self.id = id
        self.result = None
        self.metric = None
        self.parent = parent
        self.percentage = 0.0

    def run(self, data: pandas.DataFrame, weight) -> Self:
        self.result = data.sample(frac=weight, random_state=self.id)
        self.percentage = weight
        self.metric = jsh.calculate(data, self.result)
        return self

    def get_metric(self):
        return self.metric

    def get_percentage(self):
        return self.percentage

    def get_result(self):
        return self.result

    def __str__(self):
        return "s{}".format(self.id)

    def __repr__(self):
        return "s{}".format(self.id)
