class Data:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f"{self._day}/{self._month}/{self._year}"

    def next_day(self):
        self._day += 1
        return self

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        self._day = day

    @property
    def month(self):
        return self.month

    @month.setter
    def month(self, month):
        self._month = month

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, year):
        self._year = year


data = Data(29, 11, 2021)
print(data)
print(data.next_day())
data.day = 15
print(data.day)
