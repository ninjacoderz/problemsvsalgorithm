def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return binary_search_recursive(number, 2, number/2)


def binary_search_recursive(number, start_index, end_index):
    # Base case
    if number == 0 or number == 1:
        return number

    start = start_index
    end = end_index
    mid = int((start+end)/2)
    square = mid*mid
    if square == number:
        return mid
    elif square < number:
        # Check case return floor value
        if (mid+1)*(mid+1) > number:
            return mid
        return binary_search_recursive(number, mid+1, end)
    else:
        return binary_search_recursive(number, start, mid-1)
    
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")