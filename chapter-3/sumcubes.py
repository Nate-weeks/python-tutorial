# A program to calculate the sum of all cubes up to a value of n
def sumcubes():
    number = input("Enter a number for which you would like to find the sum of all the cubes up to: ")
    count = 0L
    for i in range(1, number+1):
        count += i ** 3
    return count

def test():
    print "A user input of 1, 2, 3 should be 37"
    print sumcubes()
