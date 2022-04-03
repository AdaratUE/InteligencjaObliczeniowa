import random

class Warehouse:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def generate_warehouse(ile: int = 5, ):
        dane_tmp = []
        for i in range(1, ile):
            warehouse = Warehouse(random.randrange(0, 100), random.randrange(0, 100))
            while not dane_tmp.__contains__(warehouse):
                dane_tmp.append(warehouse)
        print(dane_tmp)