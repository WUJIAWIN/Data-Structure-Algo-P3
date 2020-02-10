# Problem 3
# Rearrange Array Digits
# Expected time complexity O(nlog(n))

def rearrange_digits(input_list):
    # Merge sort the input list.
    list = sorted_list(input_list)

    # Two iterations to fit lists into two numbers.
    a = 0
    b = 0
    j = 1
    for i in list[1:len(input_list):2]:
        a += i*j
        j *= 10
    j = 1
    for i in list[0:len(input_list):2]:
        b += i*j
        j *=10

    return[a,b]

# The merge sort.
def sorted_list(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list)//2
    left = input_list[:mid]
    right = input_list[mid:]
    return merge(sorted_list(left), sorted_list(right))

# To merge two parts.
def merge(left, right):
    ans = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            ans.append(left.pop(0))
        else:
            ans.append(right.pop(0))

    ans += left
    ans += right
    return ans


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test case:
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[8], [8]])
test_function([[],[]])



