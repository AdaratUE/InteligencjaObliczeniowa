import csv

def excel_data(name: str):
    dane_tmp = []
    with open(name, newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in file:
            splited = row[0].split(';')
            dane_tmp.append(Point(splited[0], splited[1], splited[2], None))
    return dane_tmp
