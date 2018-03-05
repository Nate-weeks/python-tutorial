'''
euler9.py

A program by Nate Weeks to solve project euler problem #9
'''
#function searches for every set of numbers between 2 and 1000 such that a**2 + b**2 = c**2
#then returns the set of numbers such that a + b + c = 1000 ... very slowly
#Brute force!
def main():
    for a in range(2,1000):
        for b in range(2,1000):
            for c in range(2,1000):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        print "a: %d, b: %d, c: %d"% (a, b, c)

main()

'''
>>> python euler9.py
a: 200, b: 375, c: 425
a: 375, b: 200, c: 425
'''
