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

    def valida_dia(self):
        if self._day > 31:
            raise Exception("Dia invalido! Digite um dia entre 1 e 31")

    def valida_mes(self):
        if self._month > 12:
            raise Exception("Mes invalido! Digite um mes entre 1 e 12")

    def valida_ano(self):
        if self._year <= 0:
            raise Exception("Ano invalido! Digite um ano maior que 0 ")


data = Data(29, 11, 2021)
print(data)
print(data.next_day())
data.day = 15
print(data.day)
