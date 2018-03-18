import json
import csv

jsondata = json.load(open('data.json'))

with open('data.csv', 'a', newline='') as csvfile:
    jsonwriter = csv.writer(csvfile, delimiter=',')
    jsonwriter.writerow([jsondata['name']] + [jsondata['age']])

print(jsondata['name'])
