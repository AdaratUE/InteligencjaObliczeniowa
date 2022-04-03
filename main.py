import Point
import Warehouse
import ReadData

warehouses = []

data = ReadData.excel_data('data.csv')
data2 = Point.generate_random_data(130)
Warehouse.generate_warehouse()
