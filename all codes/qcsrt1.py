import random

def lessthan(x, y):
    return x < y

def quick_sort(arr, l, r):
    if r <= l:
        return
    # select a pivot uniformly randomly from [l, r]
    pivot_index = random.randint(l, r)
    pivot = arr[pivot_index]

    # partition_index = first index that is greater than or equal to pivot among the integers read so far
    partition_index = l
    final_position_pivot = pivot_index

    for index in range(l, r+1):
        if index != pivot_index and lessthan(arr[index], pivot):
            # swap arr[index] to the beginning of the array
            arr[index], arr[partition_index] = arr[partition_index], arr[index]
            if partition_index == final_position_pivot:
                final_position_pivot = index

            # increase partition size, more number of elements less than pivot found
            partition_index += 1

    arr[partition_index], arr[final_position_pivot] = arr[final_position_pivot], arr[partition_index]
    quick_sort(arr, l, partition_index - 1)
    quick_sort(arr, partition_index + 1, r)

# using the function
arr = [2, 3, 4, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)
