'''
remove-duplicates.py
A program to remove duplicate entries from an array
Nate Weeks, april 2018
'''

def remove_duplicates(array):
    '''
    function takes an array and removes duplicate entries
    >>> remove_duplicates([1, 2, 3, 3, 4, 1])
    [1, 2, 3, 4]
    >>> remove_duplicates(["hi", "hello", "hi theree", "hi", "bye"])
    ['hi', 'hello', 'hi theree', 'bye']
    '''
    new_array = []
    for item in array:
        if item not in new_array:
            new_array.append(item)

    return new_array

def main():
    array = [1, 2, 3, 1, 4, 4, 5]
    print "starting array:"
    print array
    print "array without duplicates: "
    print remove_duplicates(array)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
