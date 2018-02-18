'''
linearvsquadratic.py

A program to find the minimum value of an array with big O notation O(n) and O(n**2)

'''

def linear(arr):
    smallest_number = arr[0]
    for number in arr:

        if smallest_number > number:
            smallest_number = number
    print "smallest number in array with linear solution: " + str(smallest_number)

arr = [5, 13, 56, 4, 8, 17]
linear(arr)

def quadratic(arr):
    for index in range (len(arr) - 1):
        for index2 in range (len(arr) - 1):
            if arr[index2] < arr[index]:
                smallest_number = arr[index2]
    print "smallest number in array with quadratic solution: " + str(smallest_number)

quadratic(arr)

'''
>>>  algorithm-practice git:(master) python linearvsquadratic.py
smallest number in array with linear solution: 4
smallest number in array with quadratic solution: 4
'''
