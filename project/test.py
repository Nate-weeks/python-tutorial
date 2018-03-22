import json
import csv

jsondata = json.load(open('data.json'))

with open('data.csv', 'a', newline='') as csvfile:
    jsonwriter = csv.writer(csvfile, delimiter=',')
    for person in jsondata:
        for stuff in person['somestuff']:
            jsonwriter.writerow([person['name']] + [person['age']] + [person['ethnicity']]+ [stuff['otherstuff']] + [stuff['goodstuff']])



for person in jsondata:
    for stuff in person['somestuff']:
        print(person['name'], person['age'], person['ethnicity'], stuff['otherstuff'], stuff['goodstuff'])
