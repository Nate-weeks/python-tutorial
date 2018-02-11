#A program to calcule the fibonnaci sequence up to a value of n
def fibonnaci():
    number = input("enter a number for which you would like to calculate the fibonnaci sequence: ")
    prevcount = 0l
    count = 1L
    for i in range(1, number):
        prevcountersaver = count
        count = count + prevcount
        prevcount = prevcountersaver

    return count

def test():
    print "expect a user input of 6 to equal 8"
    print fibonnaci()

test()
