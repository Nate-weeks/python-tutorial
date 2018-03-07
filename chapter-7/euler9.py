'''
euler9.py

A program by Nate Weeks to solve project euler problem #9
'''
#function searches for every set of numbers between 2 and 1000 such that a**2 + b**2 = c**2
#then returns the set of numbers such that a + b + c = 1000 ... very slowly
#Brute force!
def main():
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print "a: %d, b: %d, c: %d"% (a, b, c)

main()

'''
>>> python euler9.py
a: 200, b: 375, c: 425
a: 375, b: 200, c: 425
'''
