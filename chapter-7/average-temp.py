'''
average-temp.py

A program for calculating the total heating and cooling days based on average temp

'''
#function takes a text input for filename and outputs the total number of hot days and cold days
def add_temp(filename):
    data = open(filename)
    cold_days = 0
    hot_days = 0
    for line in data:
        for string in line.split(","):
            if eval(string) >= 80:
                hot_days += eval(string)
            if eval(string) <= 60:
                cold_days += eval(string)
    return str(cold_days), str(hot_days)

print "there are: " + add_temp("data.txt")[0] + " cold days and " + add_temp("data.txt")[1] + " hot days"

'''
>>> python average-temp.py
there are: 163 cold days and 355 hot days
'''
