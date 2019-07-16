# Testing execution time of my algorithm

import time
start = time.time()


# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x 
                print(smallest_index)
        # TO-DO: swap
        # * Swap index
        # * Take the item at the current index and move it to where the smallest item was
        current_temp = arr[smallest_index]
        # ex: 3
        # * Take smallest item and put it at the current index
        arr[smallest_index] = arr[cur_index]
        # * 
        arr[cur_index] = current_temp
        # print(current_temp)
    return arr


# * Added to test out alg0
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# selection_sort(arr1)
 

# TO-DO:  implement the Bubble Sort function below
# * 
def bubble_sort( arr ):
    # swapped = ?
    for i in range(0, len(arr) - 1,1):
        # start(5),stop(1),step(1)
        for j in range(0, len(arr) - 1 - i):
           # * shows me what i and j is while running l337 h4x0rz alg0
            print(arr[i],arr[j])
           # * if arr[5] > arr[4+1]
            if arr[j] > arr[j+1]:
            # * if so Sw@p
             print(arr)
             arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# small test for bubz
# arr1 = ['b','d','f','a','c','e']
arr1 = [5,4,3,2,1]
print(bubble_sort(arr1))


ran = range(0,len(arr1) - 1)
for n in ran:
    print(n)
    
    


end = time.time()
print(end - start)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr