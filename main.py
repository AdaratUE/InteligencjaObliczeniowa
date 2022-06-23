import math
import random
import matplotlib.pyplot as plt

import Point
import Warehouse
import ReadData
from Demand import Demand
from Vehicle import Vehicle

points = ReadData.excel_data('data.csv', False)
warehouses = ReadData.excel_data('warehouse.csv', True)

# points = ReadData.generate_random_data(100)
# warehouses = ReadData.generate_warehouse(5)

vehicles = []

for i in range(0, random.randrange(3, 6)):
    type = random.randrange(0, 3)
    vehicles.append(Vehicle(type, 'vehicle' + str(i + 1), warehouses[random.randrange(0, len(warehouses))]))


def calc_dist(point1, point2):
    return math.sqrt(math.pow(int(point2.x) - int(point1.x), 2) + math.pow(int(point2.y) - int(point1.y), 2))


road = []


def calc_value(position, target, vehicle):
    dist = calc_dist(position, target)
    oranges = target.demand.oranges
    uranium = target.demand.uranium
    tuna = target.demand.tuna
    demandValue = math.fabs(oranges) + math.fabs(uranium) + math.fabs(tuna)
    if demandValue == 0:
        return 99999999999
    if target.name == vehicle.at.name:
        return 99999999999
    # resultValue = 1 / ((demandValue / (dist+1)) + 1)
    # resultValue = demandValue/(dist+1)
    resultValue = dist / demandValue
    return resultValue


def check_end():
    result = True
    for p in points:
        if (math.fabs(p.demand.oranges) + math.fabs(p.demand.uranium) + math.fabs(p.demand.tuna)) > 0:
            result = False
            break
    return result


def find_closest_warehouse(location):
    closestDist = calc_dist(location, warehouses[0])
    closestI = 0
    for w1 in range(1, len(warehouses)):
        distance = calc_dist(location, warehouses[w1])
        if distance < closestDist:
            closestDist = distance
            closestI = w1
    return closestI


def sum_all():
    sum = 0
    for p in points:
        sum += math.fabs(p.demand.oranges) + math.fabs(p.demand.uranium) + math.fabs(p.demand.tuna)
    return sum


roads = []

for tr in range(0, len(vehicles)):
    roads.append([[], vehicles[tr]])

while not check_end():
    for truck in range(0, len(vehicles)):
        minPoint = points[0]
        minGlobal = calc_value(vehicles[truck].at, points[0],
                               vehicles[truck])  # calc_dist(vehicles[0].at, points[0])
        minI = 0
        for i in range(1, len(points)):
            if vehicles[truck].at.name == points[i].name:
                continue

            minV = calc_value(vehicles[truck].at, points[i], vehicles[truck])  # calc_dist(vehicles[0].at, points[i])

            if minV < minGlobal:
                minGlobal = minV
                minPoint = points[i]
                minI = i

        if vehicles[truck].at.demand is None:

            vehicles[truck].load(0, points[minI].demand.oranges + 50)
            vehicles[truck].load(1, points[minI].demand.uranium + 50)
            vehicles[truck].load(2, points[minI].demand.tuna + 50)
            vehicles[truck].at = minPoint

        else:
            # print(points[minI].demand)
            if points[minI].demand.oranges < 0:
                # print(vehicles[truck].load(0, points[minI].demand.oranges))
                points[minI].demand.oranges -= vehicles[truck].load(0, points[minI].demand.oranges)
                vehicles[truck].at = minPoint
            else:
                vehicles[truck].at = minPoint
                points[minI].demand.oranges -= vehicles[truck].unload(0, points[minI].demand.oranges)

            if points[minI].demand.uranium < 0:
                # print(vehicles[truck].load(0, points[minI].demand.uranium))
                points[minI].demand.uranium -= vehicles[truck].load(0, points[minI].demand.uranium)
                vehicles[truck].at = minPoint

            else:
                vehicles[truck].at = minPoint
                points[minI].demand.uranium -= vehicles[truck].unload(0, points[minI].demand.uranium)

            if points[minI].demand.tuna < 0:
                # print(vehicles[truck].load(0, points[minI].demand.uranium))
                points[minI].demand.tuna -= vehicles[truck].load(2, points[minI].demand.tuna)
                vehicles[truck].at = minPoint
            else:
                vehicles[truck].at = minPoint
                points[minI].demand.tuna -= vehicles[truck].unload(0, points[minI].demand.tuna)

        if vehicles[truck].load_warehouse():
            vehicles[truck].at = warehouses[find_closest_warehouse(vehicles[truck].at)]
        if vehicles[truck].unload_warehouse():
            vehicles[truck].at = warehouses[find_closest_warehouse(vehicles[truck].at)]
        # road.append(vehicles[truck].at.name)
        road.append(vehicles[truck].at)

    for tr in range(0, len(vehicles)):
        roads[tr][0].append(road[tr])
    road = []
    sum = 0

plt.figure(figsize=[15, 15])
plt.suptitle('Trasy\n')
sub = 1

for road1 in roads:
    print([i.name for i in road1[0]])
    plt.subplot(3, 2, sub)
    plt.title(f'Trasa pojazdu nr {sub}')
    plt.xlabel('współrzędna x')
    plt.ylabel('współrzędna y')
    plt.xticks([0, 25, 50, 75, 100])
    plt.yticks([0, 25, 50, 75, 100])
    x = [int(i.x) for i in road1[0]]
    y = [int(i.y) for i in road1[0]]
    plt.plot(x, y, 'o--r', ms=10, alpha=.3)
    sub += 1

plt.savefig('trasy.png')
plt.show()
