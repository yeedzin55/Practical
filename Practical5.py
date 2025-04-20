# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index if the target is found
#     return -1  # Return -1 if the target is not in the list

# # Test the function
# test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# result = linear_search(test_list, 6)
# print(f"Linear Search: Index of 6 is {result}")
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid  # Return the index if the target is found
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return -1  # Return -1 if the target is not in the list

# # Test the function
# test_list_sorted = sorted(test_list)
# result = binary_search(test_list_sorted, 6)
# print(f"Binary Search: Index of 6 in sorted list is {result}")
# import time

# def compare_search_algorithms(arr, target):
#     # Linear Search
#     start_time = time.time()
#     linear_result = linear_search(arr, target)
#     linear_time = time.time() - start_time
    
#     # Binary Search (on sorted array)
#     arr_sorted = sorted(arr)
#     start_time = time.time()
#     binary_result = binary_search(arr_sorted, target)
#     binary_time = time.time() - start_time
    
#     print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
#     print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# # Test with a larger list
# large_list = list(range(10000))
# compare_search_algorithms(large_list, 8888)
# def binary_search_recursive(arr, target, left, right):
#     if left > right:
#         return -1
    
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, right)
#     else:
#         return binary_search_recursive(arr, target, left, mid - 1)

# # Test the recursive function
# result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
# print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")
# def main():
#     # Create a list of 20 random integers between 1 and 100
#     import random
#     test_list = [random.randint(1, 100) for _ in range(20)]
    
#     print("Original list:", test_list)
#     print("Sorted list:", sorted(test_list))
    
#     target = random.choice(test_list)  # Choose a random target from the list
#     print(f"\nSearching for: {target}")
    
#     # Linear Search
#     result = linear_search(test_list, target)
#     print(f"Linear Search: Found at index {result}")
    
#     # Binary Search (iterative)
#     sorted_list = sorted(test_list)
#     result = binary_search(sorted_list, target)
#     print(f"Binary Search (iterative): Found at index {result}")
    
#     # Binary Search (recursive)
#     result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
#     print(f"Binary Search (recursive): Found at index {result}")
    
#     # Compare performance
#     print("\nPerformance Comparison:")
#     compare_search_algorithms(list(range(100000)), 99999)

# if __name__ == "__main__":
#     main()


# Exercise
# Modifying the linear search to return all indices

test_list = [2, 5, 3, 9, 7, 6, 1, 4]

def linear_search_to_return_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

print(linear_search_to_return_all_indices(test_list, 2))  
print(linear_search_to_return_all_indices(test_list, 9))  
print(linear_search_to_return_all_indices(test_list, 1)) 

#Implementing binary search to find the insertion point
def find_insertion_point(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

print(find_insertion_point(test_list, 1))  
print(find_insertion_point(test_list, 0))  
print(find_insertion_point(test_list, 5)) 

# counting the number of comparisons made in each search algorithm
def linear_search_with_count(arr, target):
    
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search_with_count(arr, target):
    
    comparisons = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

print(linear_search_with_count(test_list, 7))  
print(binary_search_with_count(test_list, 7))
print(linear_search_with_count(test_list, 9))  
print(binary_search_with_count(test_list, 9))  

#Implementing a jump search algorithm and compare its performance with linear and binary search

import math

def jump_search(arr, target):
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Find the block where target might be
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    return -1

# Performance comparison function
def compare_search_algorithms(arr, target):
    """Compares linear, binary, and jump search"""
    # Linear search
    linear_result, linear_comparisons = linear_search_with_count(arr, target)
    
    # Binary search (requires sorted array)
    sorted_arr = sorted(arr)
    binary_result, binary_comparisons = binary_search_with_count(sorted_arr, target)
    
    # Jump search (requires sorted array)
    jump_comparisons = 0
    n = len(sorted_arr)
    step = int(math.sqrt(n))
    prev = 0
    jump_comparisons += 1
    
    # Count comparisons in jump phase
    while sorted_arr[min(step, n)-1] < target:
        jump_comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            jump_comparisons += 1
            break
    
    # Count comparisons in linear phase
    if prev < n:
        while sorted_arr[prev] < target:
            jump_comparisons += 1
            prev += 1
            if prev == min(step, n):
                jump_comparisons += 1
                break
        jump_comparisons += 1  # For the final equality check
    
    jump_result = jump_search(sorted_arr, target)
    
    print(f"Searching for {target} in array of size {len(arr)}")
    print(f"Linear search: {linear_comparisons} comparisons, result: {linear_result}")
    print(f"Binary search: {binary_comparisons} comparisons, result: {binary_result}")
    print(f"Jump search: ~{jump_comparisons} comparisons, result: {jump_result}")

# Example usage:
data = [i for i in range(1, 100)]  # Numbers 1-99
compare_search_algorithms(data, 42)
compare_search_algorithms(data, 101)