def linear_search(arr, target):

    # declare index variable
    i = 0

    # iterate through each element in array
    for e in arr:
        # if it equals the target return the index
        if e == target:
            return i
        # increment index
        i += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # make the midpoint be the sum of high and low divided by two
        mid = (high + low) // 2
        
        # if the target is the mid value then rturn it
        if target == arr[mid]:
            return mid
            
        # if the target is less than the midpoint, it must be on the left side, so make the new highpoint into the current midpoint exclusively
        if target < arr[mid]:
            high = mid - 1

        # if the target is greater than the midpoint, go right, so make the new low point into the current midpoint + 1
        if target > arr[mid]:
            low = mid + 1

    return -1  # not found
