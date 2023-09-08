def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        print("List must be not empty")
        return None

    minn, maxx = (ints[0], ints[0])
    for value in ints:
        if minn > value:
            minn = value
        if maxx < value:
            maxx = value
    return (minn, maxx)

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Test case 2
l2 = []
get_min_max(l2) # Print: "List must be not empty

# Test case 3
l2 = None
get_min_max(l2) # Print: "List must be not empty
