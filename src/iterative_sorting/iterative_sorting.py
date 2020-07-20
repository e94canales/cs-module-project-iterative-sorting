# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # sets a boundary to keep track of where we're at, starts with 0
        boundary = i
        
        # initialize the smallest values as the current boundary
        smallest_value = arr[boundary]
        smallest_index = boundary
  
        # iterates through the unsorted "right" side of the array, starting with boundary
        for e in range(boundary, len(arr)): 
            if arr[e] < smallest_value:
                # sets the new smallest value
                smallest_value = arr[e]
                # sets the new smallest index
                smallest_index = e
                
        # swap the two indexes in the array
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    for i in range(len(arr) - 1):
        # iterate and check to see if index(x) is greater than index(x + 1)
        for e in range(len(arr) - 1):
            if arr[e] > arr[e + 1]:
                # if it is greater. switch the numbers so that the smallest is on the left
                arr[e], arr[e + 1] = arr[e + 1], arr[e]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
