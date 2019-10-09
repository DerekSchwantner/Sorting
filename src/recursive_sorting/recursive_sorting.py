unsrted_nums = [1, 2, 5]
nums2 = [3, 9, 12, 25]

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            merged_arr[i] = arrB[0]
            del arrB[0]


    return merged_arr

print(merge(unsrted_nums, nums2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        slice_point = round(len(arr) / 2)
        arrA = arr[0:slice_point]
        arrB = arr[slice_point:]
        arr = merge(merge_sort(arrA), merge_sort(arrB))

    return arr

test = [3, 79, 99, 54, 1, 4, 6, 11]
print(merge_sort(test))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[-1]
#     left = []
#     right = []
#     for i in range(len(arr) - 1):
#         array = arr[i]
#         if array < pivot:
#             left.append(array)
#         else:
#             right.append(array)
#
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
#
# print(quick_sort(unsrted_nums))




# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     # TO-DO
#     for i in range(elements):
#         # check if there are empty lists, if so use first element of other list and delete first element from other list
#         if len(arrA) == 0:
#             merged_arr[i] = arrB[0]
#             del arrB[0]
#         elif len(arrB) == 0:
#             merged_arr[i] = arrA[0]
#             del arrA[0]
#         # if both lists have elements, compare first element of each list, set that element to merged[i] and delete that element from original
#         elif arrA[0] < arrB[0]:
#             merged_arr[i] = arrA[0]
#             del arrA[0]
#         else:
#             merged_arr[i] = arrB[0]
#             del arrB[0]
#
#     return merged_arr
