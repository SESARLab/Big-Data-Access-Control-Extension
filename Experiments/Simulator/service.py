import pandas
import numpy
from profiles import PregeneratedProfiles, ServiceProfile
from metrics.jsh import calculate


class Service():
    def __init__(self, id, profile: ServiceProfile = PregeneratedProfiles.GOOD):
        self.id = id
        self.result = None
        self.metric = None
        self.profile: ServiceProfile = profile

    def run(self, data: pandas.DataFrame):
        # print("\tService s{} running".format(self.id))
        numpy.random.seed(self.id)
        sample_size = numpy.random.uniform(self.profile.getMin(), self.profile.getMax())
        # print("\t\tsampling {}% of data".format(sample_size * 100))
        self.result = data.sample(frac=sample_size, random_state=self.id)
        self.metric = calculate(data, self.result)
        # print("\t\ts{} finished - metric: {}".format(self.id, self.metric))
        return self

    def get_metric(self):
        return self.metric

    def get_result(self):
        return self.result

    def __str__(self):
        return "s{} ".format(self.id)

    def __repr__(self):
        return "s{} ".format(self.id)
