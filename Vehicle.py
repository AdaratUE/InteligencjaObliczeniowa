from Point import Point


class Vehicle:
    def __init__(self, type: int, name: str, at: Point):
        self.type = type
        self.name = name
        self.at = at
        if type == 2:
            self.cap = 2000
        elif type == 1:
            self.cap = 1500
        else:
            self.cap = 1000

