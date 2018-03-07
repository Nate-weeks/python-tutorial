def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_array(arr[1:])

print sum_array([2,4,6,8])
