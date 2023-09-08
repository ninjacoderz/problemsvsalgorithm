def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    "Boundary cases"

    if input_list is None or len(input_list) <= 1:
        return [None, None]
    
    marker = [0] * 10
    for input in input_list:
        marker[input] += 1

    # check even/odd array
    type_even = True
    if len(input_list) % 2 == 1:
        type_even = False
    # Add the digits to the 2 arrays in descending order
    num_1 = []
    num_2 = []
    digit = 9 # digit start from 0 
    while digit >= 0:
        while marker[digit] > 0:
            if type_even:
                num_1.append(digit)
                type_even = False
            else:
                num_2.append(digit)
                type_even = True
            marker[digit] -= 1
        digit -= 1
    return [array_to_int(num_1), array_to_int(num_2)]

def array_to_int(array):
    output = 0
    for a in array:
        output = output*10+a
    return output   

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [954, 862]])

# Test case 3
print(rearrange_digits([1]))  # [None, None]

# Test case 4
print(rearrange_digits([]))  # [None, None]

# Test case 5
print(rearrange_digits([3, 5]))  # [5, 3]
