import random
from Demand import Demand

class Point:
    def __init__(self, name: str, x: int, y: int, goods: list):
        self.x = x
        self.y = y
        self.name = name
        #self.goods = goods
        self.demand = Demand()

    def __str__(self):
        return self.demand.oranges.__str__() + " "+self.demand.uranium.__str__() + " "+self.demand.tuna.__str__()
