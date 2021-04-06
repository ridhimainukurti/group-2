import statistics

class numberlist:
    def __init__(self, series):
        if series < 0 or series > 1000:
            return ValueError("Number is not between 0 and 1000")
        self.series = series
        self._list = []
        self._dict = {}

