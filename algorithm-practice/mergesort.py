'''
mergsort.py A program to sort an array of integers by
Nate Weeks
code example largely taken from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
'''
''' given an input of a list of integers, split them in half until
they are only 1 element long, then merge them'''
def sort(alist):
    print("Splitting ",alist)
    if len(alist)>1:    # base case
        mid = len(alist)//2  # mid-point to split the array
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # call sort on both halves of the array
        sort(lefthalf)
        sort(righthalf)
        # merge the split up arrays
        merge(lefthalf, righthalf, alist)

# given two arrays, merge them from smallest to largest
def merge(array1, array2, result):
    i=0     # initial starting index of array1
    j=0     # initial starting index of array2
    k=0     # initial index of resulting array

    # while there are items in each array merge them in order
    # from smallest to largest
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result[k]=array1[i]
            i=i+1
        else:
            result[k]=array2[j]
            j=j+1
        k=k+1

    #handle for the case where array2 is empty
    while i < len(array1):
        result[k]=array1[i]
        i=i+1
        k=k+1

    #handle for the case where array1 is empty
    while j < len(array2):
        result[k]=array2[j]
        j=j+1
        k=k+1
    print("Merging ",result)

alist = [54,26,93,17,77,31,44,55,20]
sort(alist)
print(alist)
