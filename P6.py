# Problem 6
# Unsorted Integer Array
# Expected run time O(n).

def get_min_max(ints):
    if len(ints) == 0:
        return None

    min = ints[0]
    max = ints[0]
    for num in ints:
        if num >= max:
            max = num
        elif num <= min:
            min = num
        else:
            continue
    return(min, max)


# Test cases
# case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# case 2
l = [i for i in range(-5, 10)]
print ("Pass" if ((-5, 9) == get_min_max(l)) else "Fail")

# case 3
l = []
print ("Pass" if None == get_min_max(l) else "Fail")


