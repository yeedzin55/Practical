# # implement bubble sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# # Test the function
# test_arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(test_arr.copy())
# print("Bubble Sort Result:", sorted_arr)

# # implement merge sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
    
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i, j = 0, 0
    
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# # Test the function
# test_arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = merge_sort(test_arr)
# print("Merge Sort Result:", sorted_arr)

# # implement quick sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr[1:] if x <= pivot]
#         greater = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)

# # Test the function
# test_arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = quick_sort(test_arr)
# print("Quick Sort Result:", sorted_arr)

# # comparing performance
# import time
# import random

# def compare_sorting_algorithms(arr):
#     algorithms = [
#         ("Bubble Sort", bubble_sort),
#         ("Merge Sort", merge_sort),
#         ("Quick Sort", quick_sort)
#     ]
    
#     for name, func in algorithms:
#         arr_copy = arr.copy()
#         start_time = time.time()
#         func(arr_copy)
#         end_time = time.time()
#         print(f"{name} took {end_time - start_time:.6f} seconds")

# # Generate a large random array
# large_arr = [random.randint(1, 1000) for _ in range(1000)]

# # Compare the algorithms
# compare_sorting_algorithms(large_arr)



# Exercise

# implementing in place  version of quick sort
#Traditional Quick Sort uses O(n) extra space in worst case due to recursion
# This in-place version modifies the original array without creating new arrays
# Uses O(log n) space for recursion stack (best/average case)
# The partition function selects a pivot and rearranges elements around it

nums = [1, 5, 0, 2, 4, 3]

def quick_sort_in_place(arr, low, high):                                      
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot
    return i + 1

quick_sort_in_place(nums, 0, len(nums) - 1)
print("quick_sort_in_place):", nums)

#modifying bubble sort (early termination)
# Standard Bubble Sort always makes n passes
# This version adds a swapped flag to detect if any swaps occurred
# If no swaps in a pass, the array is sorted and we can terminate early
# Best case (already sorted) becomes O(n) instead of O(n²)

def bubble_sort_modified(arr):
   
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break
bubble_sort_modified(nums)
print("Modified Bubble Sort:", nums)

# Implementing a hybrid sorting algorithm (Merge Sort + Insertion Sort for small arrays)
# Merge Sort has overhead for small arrays
# This hybrid switches to Insertion Sort when subarrays are small (≤ threshold)
# Insertion Sort is faster for small arrays due to lower constant factors
# Combines O(n log n) worst-case of Merge Sort with O(n²) but fast Insertion Sort for small n

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr, left, right):
    if right - left <= 10:
        insertion_sort(arr, left, right)
    else:
        mid = (left + right) // 2
        hybrid_merge_sort(arr, left, mid)
        hybrid_merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

hybrid_merge_sort(nums, 0, len(nums) - 1)
print("Hybrid Merge+Insertion Sort:", nums)

#Sorting Algorithm Visualizations with Matplotlib
# Creates animated bar charts showing the sorting process
# Each algorithm is modified to yield its state after each operation
# Highlights elements being compared/swapped in red
# Tracks and displays comparison and swap counts
# Can be adapted for other algorithms by:
# Creating a generator version of the algorithm
# Yielding state after each significant operation
# Including what elements to highlight

