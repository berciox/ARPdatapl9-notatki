import math
import openpyxl
import numpy as np

# funkcja do obliczania odległości między dwoma punktami
def distance(p1, p2):
    return math.sqrt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 + (p1[3]-p2[3])**2)

# wczytaj współrzędne punktów z pliku txt
with open('1904CONV2.txt', 'r') as file:
    lines = file.readlines()

# zapisz współrzędne punktów do listy
points = []
for line in lines:
    line = line.strip().split(' ')
    point = (line[0], float(line[1]), float(line[2]), float(line[3]))
    points.append(point)

# oblicz odległości między punktami
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        d = distance(points[i], points[j])
        distances.append((points[i][0]+'-'+points[j][0], d))

# utwórz arkusz Excel i zapisz wyniki
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'Odległości'
worksheet.decimal_separator = ','

# zapisz wyniki w arkuszu Excel
data = np.array(distances)
data_t = data.transpose()
for i in range(len(data_t)):
    for j in range(len(data_t[i])):
        value = data_t[i][j]
        cell = worksheet.cell(row=i+1, column=j+1)
        cell.value = value


# zapisz arkusz Excel do pliku
workbook.save('odleglosci.xlsx')