import time
start = time.time()



# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
 #Arrays already sorted! no need < JK!
 # Using list and sort works but removes all duplicates and in this case we want all those
 # but just sorted

 # merged_arr = list(set(arrA + arrB))
    i = 0
    j = 0
    idx = 0
    # TO-DO
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[idx] = arrA[i]
            i += 1
        else:
            merged_arr[idx] =  arrB[j]
            j += 1
        idx += 1
    while i < len(arrA):
        merged_arr[idx] = arrA[i]
        i += 1
        index += 1
    while j < len(arrB):
        merged_arr[idx] = arrB[j]
        j += 1
        idx += 1

 
    print(merged_arr)

    return merged_arr


arr1 = [0,1,2,3,7,4,8,9,2,3,1,2,0]
arr2 = [4,5,6,1,1,1]

merge(arr1,arr2)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if greater than 1 lets split it otherwise no need to merge and sort 1 value
    if len(arr) < 2:
        return arr
        #split into individual arr?
        # split into 2 arr and sort
    else:
            middle = int(len(arr) //2) #pivot?  
            left_arr = merge_sort(arr[:middle])
            right_arr = merge_sort(arr[middle:])
        # merge into arr of 2 and with smallest of the 2 num first
            return merge(left,right)

    return arr








# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr




end = time.time() 
print(end - start) 



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
