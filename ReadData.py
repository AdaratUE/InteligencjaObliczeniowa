import csv
import random

from Point import Point
from Warehouse import Warehouse


def excel_data(name: str, warehouse: bool):
    tmp = []
    with open(name, newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in file:
            splited = row[0].split(';')
            if warehouse:
                tmp.append(Warehouse(splited[0], splited[1], splited[2], None))
            else:
                tmp.append(Point(splited[0], splited[1], splited[2], None))
    return tmp


def generate_random_data(how_many: int):
    tmp = []
    for i in range(1, how_many):
        tmp.append(Point("Point" + i.__str__(), random.randrange(0, 100), random.randrange(0, 100), None))
    return tmp



def generate_warehouse(how_many: int):
    tmp = []
    for i in range(1, how_many):
        warehouse = Warehouse("Warehouse" + i.__str__(), random.randrange(0, 100), random.randrange(0, 100), None)
        while not tmp.__contains__(warehouse):
            tmp.append(warehouse)
    return tmp