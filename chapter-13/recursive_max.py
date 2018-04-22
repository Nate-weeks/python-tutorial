'''
recursive_max.py
A recursive program for finding the max value in a list
Nate Weeks, april 2018
'''

def recursive_max(array):
    '''
    function that takes an array and returns the max value
    >>> recursive_max([1,2,3,4,5,6,7])
    7
    '''
    if len(array) == 1:
        return array[0]
    else:
        return max(array[0], recursive_max(array[1:]))

def main():
    array = [1,4,11,7,9,3]
    print recursive_max(array)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
