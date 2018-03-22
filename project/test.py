import json
import csv

jsondata = json.load(open('data.json'))

with open('data.csv', 'a', newline='') as csvfile:
    jsonwriter = csv.writer(csvfile, delimiter=',')


    jsonwriter.writerow([jsondata['name']] + [jsondata['age']] + [jsondata['somestuff']['otherstuff']])


for person in jsondata:
    print(person['age'], person['ethnicity'])
    for stuff in person['somestuff']:
        print(stuff['otherstuff'])
