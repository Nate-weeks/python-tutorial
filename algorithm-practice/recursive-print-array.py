'''
program to recursively print an array
Nate Weeks
'''

def recursive_print(arr):
    if len(arr) == 0:
        return ""
    else:
        print arr[0]
        return recursive_print(arr[1:])

recursive_print([3, 5, 8, 9])
