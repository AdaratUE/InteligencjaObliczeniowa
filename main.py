import math
import random

import Point
import Warehouse
import ReadData
from Demand import Demand
from Vehicle import Vehicle

points = ReadData.excel_data('data.csv', False)
warehouses = ReadData.excel_data('warehouse.csv', True)

# points = ReadData.generate_random_data(100)
# warehouses = ReadData.generate_warehouse(5)

dem = Demand(points)

for idx, point in enumerate(points):
    point.goods = dem.demand()[idx]

vehicles = []

for i in range(0, random.randrange(3, 6)):
    type = random.randrange(0, 3)
    vehicles.append(Vehicle(type, 'vehicle' + str(i + 1), warehouses[random.randrange(0, len(warehouses))]))


def calc_dist(point1, point2):
    return math.sqrt(math.pow(int(point2.x) - int(point1.x), 2) + math.pow(int(point2.y) - int(point1.y), 2))


road = []

for k in range(0, 10):
    min = calc_dist(vehicles[0].at, points[0])
    minPoint = points[0]
    prevPoint = points[0]

    for i in range(1, len(points)):
        minTmp = calc_dist(vehicles[0].at, points[i])
        print("min:" + prevPoint.name)
        print(points[i].name)
        if prevPoint.name == points[i].name:
            continue
        if minTmp < min:
            minPoint = points[i]
            min = minTmp

    # print(minPoint.name)
    # print(vehicles[0].at.name)
    print(minPoint.name)
    print(vehicles[0].at.name)
    vehicles[0].at = minPoint
    prevPoint = minPoint
    road.append(minPoint.name)

print(road)
