'''
shuffle.py
A program by Nate Weeks to shuffle an array
April 2018
'''
import random


def shuffle(array):
    ''' Takes an array and shuffles the items into a random order'''
    for index in range(len(array) - 1):
        rand = random.randint(1,len(array) - 1)  # random index -1 to accurately reflect index
        array[index], array[rand] = array[rand], array[index]
    return array

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print "expect each array to be randomly different"
    print "starting array: "
    print array
    print "shuffled arrays:"
    for i in range(10):
        print shuffle(array)


if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
