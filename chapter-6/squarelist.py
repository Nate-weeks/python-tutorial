'''
sumlist.py

by Nate Weeks
'''

#function to take a list of integers and return the square of each integer

def squareEach(nums):
    '''
    >>> squareEach([2, 4, 6])
    [4, 16, 36]
    '''
    squaredArray = map(lambda x: x**2, nums)
    return squaredArray

def main():
    arr = [4, 5, 6]
    print squareEach(arr)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()

'''
>>>v chapter-6 git:(master) - python squarelist.py
[16, 25, 36]
'''
