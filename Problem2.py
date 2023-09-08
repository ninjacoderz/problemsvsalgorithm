def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None or len(input_list) == 0:
        return -1

    length = len(input_list)
    pivot = find_pivot(input_list, 0, length-1)

    # All array are sorted
    if pivot == -1:
        return binary_search_recursive(input_list, number, 0, length-1)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search_recursive(input_list, number, 0, pivot-1)
    return binary_search_recursive(input_list, number, pivot + 1, length-1)

# Get pivot position
def find_pivot(array, left, right):
    if left == right:
        return left
    elif left > right:
        return -1

    mid = int((left + right)/2)

    if mid > left and array[mid-1] > array[mid]:
        return mid-1
    if right > mid and array[mid] > array[mid + 1]:
        return mid
    if array[mid] > array[left]:
        return find_pivot(array, mid + 1, right)
    return find_pivot(array, left, mid-1)

# Binary search
def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(array, target, mid_index + 1, end_index)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test 1
print(rotated_array_search([], 5))

# Test 2
print(rotated_array_search(None, 4))

# Test 3
print(rotated_array_search([10], 10))

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])