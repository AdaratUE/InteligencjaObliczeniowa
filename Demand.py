import random


class Demand:
    def __init__(self):
        self.check = random.randint(100, 200)
        self.oranges = random.randint(0, self.check)
        self.check -= self.oranges
        self.tuna = random.randint(0, self.check)
        self.check -= self.tuna
        self.uranium = self.check

        if random.random() < .5:
            self.oranges = self.oranges*-1

        if random.random() < .5:
            self.uranium = self.uranium*-1

        if random.random() < .5:
            self.tuna = self.tuna*-1

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

    def value(self):
        return self.tuna + self.uranium + self.oranges

    def __str__(self):
        return self.oranges.__str__() + " "+self.uranium.__str__() + " "+self.tuna.__str__()