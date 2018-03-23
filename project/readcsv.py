import csv
from collections import Counter


with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    array = []
    for row in reader:
        for column in row:
            array.append(column)
    c = Counter(array)
csvfile.close()
data = open('data.txt', 'w')
data.write('%d\n15 %d\nlatino %d\notherstuff %d\ngoodstuff %d' % (c['nate'],c['15'],c['latino'], c['otherstuff'], c['goodstuff']))
data.close()
