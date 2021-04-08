class Addition:

    def __init__(self, series):
        if series < 0 or series > 10:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._gracevar = 6
        self._list = []
        self._dict = {}
        self._dictID = 0

        self.additionseries()


    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def additionseries(self):
        # limit = self._series
        limit = self._gracevar
        f = [0, self._series]
        for i in range(0,limit + 1):
            self.set_data(f[0])
            f = [f[0] + self._series]

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        # self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._list.append(num)
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._gracevar
       # return self._series + 3

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    n = self._gracevar + 2

    addition = Addition(n)
    print("hello world.")
    print(f"Addition of {n} = {addition.number}")
    print(f"Addition series for {n} = {addition.list}")



    for i in range(0 ,  10):
        print(f"Adding sequence {i} = {addition.get_sequence(i)}")
