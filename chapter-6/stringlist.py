'''
stringlist.py - A program for converting strings into numbers
by nate Weeks
'''

# function to transform a list of numeric strings into a list of integers
def numbers(stringlist):
    '''
    >>> numbers(["1", "2", "3", "4"])
    [1, 2, 3, 4]
    '''
    numberlist = map(int, stringlist)
    return numberlist

def main():
    stringlist = ["12", "9", "13", "8"]
    integers = numbers(stringlist)
    print integers

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()

'''
output
>>> chapter-6 git:(master) - python stringlist.py
[12, 9, 13, 8]
'''
