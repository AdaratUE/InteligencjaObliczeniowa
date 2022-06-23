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
        self.oranges = 0
        self.uranium = 0
        self.tuna = 0

    def count(self):
        return self.oranges + self.uranium + self.tuna

    def load(self, material, quantity) -> int:
        if quantity >= 0:
            if material == 0:
                if (quantity + self.count()) < self.cap:
                    self.oranges += quantity
                    return quantity
                else:
                    value = (quantity + self.count()) - self.cap
                    self.oranges += quantity - ((quantity + self.count()) - self.cap)
                    return value
            if material == 1:
                if (quantity + self.count()) < self.cap:
                    self.uranium += quantity
                    return quantity
                else:
                    self.uranium += quantity - ((quantity + self.count()) - self.cap)
                    return (quantity + self.count()) - self.cap
            if material == 2:
                if (quantity + self.count()) < self.cap:
                    self.tuna += quantity
                    return quantity
                else:
                    self.uranium += quantity - ((quantity + self.count()) - self.cap)
                    return (quantity + self.count()) - self.cap
        return quantity

    def unload(self, type: int, quantity: int):
        if type == 0:
            if (self.oranges - quantity) >= 0:
                self.oranges -= quantity
                return -quantity
            else:
                value = quantity - (self.oranges - quantity)
                self.oranges += -(self.oranges - quantity)
                return value

        if type == 1:
            if (self.uranium - quantity) >= 0:
                self.uranium -= quantity
                return -quantity
            else:
                value = quantity - (self.uranium - quantity)
                self.uranium += -(self.uranium - quantity)
                return value

        if type == 2:
            if (self.tuna - quantity) >= 0:
                self.tuna -= quantity
                return -quantity
            else:
                value = quantity - (self.tuna - quantity)
                self.tuna += -(self.tuna - quantity)
                return value

    def unload_warehouse(self):
        if self.count() > self.cap * 0.9:
            return True
        else:
            return False

    def load_warehouse(self):
        if self.count() < self.cap * 0.05:
            return True
        else:
            return False
