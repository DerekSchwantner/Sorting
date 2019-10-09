unsrted_nums = [44, 53, 2, 1, 600, 76, 23, 90]
unsrted_names = ["don", "al", "zed", "tim", "babs", "carl", "frank", "lucy"]


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for n in range(i, len(arr)):
            if arr[n] < arr[smallest_index]:
                # print(f"swapped: {arr[smallest_index]} for {arr[n]}")
                smallest_index = n


        # TO-DO: swap
        arr[smallest_index],arr[cur_index] = arr[cur_index],arr[smallest_index]

    return arr




# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        count = 0
        for n in range(0, len(arr) - 1):
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]


    return arr

print(bubble_sort(unsrted_nums))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



# print(selection_sort(unsrted_names))



