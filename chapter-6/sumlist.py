'''
sumlist.py
by Nate Weeks
'''

#function to take an array of integers and return the sum of all integers in the array

def sumList(nums):
    '''
    >>> sumList([12, 10, 8])
    30
    '''
    sum = 0
    for num in nums:
        sum += num
    return sum

def main():
    arr = [23, 25, 89, 24]
    print sumList(arr)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()

'''
>>> chapter-6 git:(master) - python sumlist.py
161
'''
