import random

class ServiceProfile:

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def __repr__(self):
        return "ServiceProfile(min={},max={})".format(self.min, self.max)

    def __str__(self):
        return "ServiceProfile(min={},max={})".format(self.min, self.max)

    def __eq__(self, other):
        return self.min == other.min and self.max == other.max


class PregeneratedProfiles:
    GOOD = ServiceProfile(0.9, 1)
    MEDIUM = ServiceProfile(0.5, 0.8)
    BAD = ServiceProfile(0.01, 0.4)
    RANDOM = ServiceProfile(0.01, 1)

