import random


class Demand:
    def __init__(self, points):
        self._points = points
        self._oranges = 0
        self._uranium = 0
        self._tuna = 0
        self._check = 0
        self.dem = []

    @property
    def points(self):
        return self._points

    @property
    def oranges(self):
        return self._oranges

    @property
    def uranium(self):
        return self._uranium

    @property
    def tuna(self):
        return self._tuna

    @property
    def check(self):
        return self._check

    @oranges.setter
    def oranges(self, value) -> None:
        self._oranges = value

    @uranium.setter
    def uranium(self, value) -> None:
        self._uranium = value

    @tuna.setter
    def tuna(self, value) -> None:
        self._tuna = value

    @check.setter
    def check(self, value) -> None:
        self._check = value

    def _demand(self) -> dict:
        shipping = random.choice([-1, 1])
        self.check = random.randint(100, 200)
        self.oranges = random.randint(0, self.check)
        self.check -= self.oranges
        self.tuna = random.randint(0, self.check)
        self.check -= self.tuna
        self.uranium = self.check
        return {'shipping': shipping, 'oranges': shipping * self.oranges, 'tuna': shipping * self.tuna,
                'uranium': shipping * self.uranium}

    def demand(self):
        for i in self.points:
            self.dem.append(self._demand())
        return self.dem

    def __str__(self):
        form = f"Demand for points: "
        for i in self.dem:
            form += str(i) + '\n'
        return form
