import statistics

class numlist:
    def __init__(self):
        self._lst=[]

    def average(self):
        mean = sum(self._lst) / len(self._lst)
        return round(mean, 2)


    def value1(self, value):
        self._lst.append(value)

    def values2(self, values):
        for value in values.split(","):
            self._lst.append(int(value))

    def median(self):
        self._lst.sort()
        mid = len(self._lst) // 2
        if mid == 0:
            return 0
        return (self._lst[mid] + self._lst[~mid]) / 2

    def mode(self):
        return statistics.mode(self._lst)

    def list(self):
        s = ','
        return s.join(str(value) for value in self._lst)