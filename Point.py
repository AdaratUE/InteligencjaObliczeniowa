import random

class Point:
    def __init__(self, nazwa: str, x: int, y: int, towary: list):
        self.x = x
        self.y = y
        self.nazwa = nazwa
        self.towary = towary

    def generate_random_data(ile: int):
        dane_tmp = []
        for i in range(1, ile):
            dane_tmp.append(Point("Point" + i.__str__(), random.randrange(0, 100), random.randrange(0, 100), None))
        return dane_tmp
