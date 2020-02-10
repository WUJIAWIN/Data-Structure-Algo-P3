# Problem 2 Search in a Rotated Sorted Array
# Runtime complexity must be O(log(n)).

def rotated_array_search(input_list, number):
    # Use a helper function to return the index of maximum number
    if input_list == []:
        return -1
    if len(input_list) ==1:
        if number == input_list[0]:
            return 0
        else:
            return -1

    max_index = find_max(input_list)

    if number == input_list[max_index]:
        return max_index

    # Given the location of max number,we can narrow down the array and /
    # /use binary search to find the target number.
    left = 0
    right = len(input_list) -1

    # After the comparison, we can pin to the left or right array.
    if number > input_list[0]:
        right = max_index
    elif number < input_list[-1]:
        left = max_index

    # Binary search
    while left <= right:
        mid = ((left + right) // 2)
        if left == mid and input_list[mid]!= number:
            return -1
        elif number ==input_list[mid]:
            return mid
        elif input_list[mid] < number:
            left = mid
            mid = (left + right) // 2
        elif input_list[mid] > number:
            right = mid
            mid = (left + right) // 2

def find_max(input_list):
    left = 0
    right = len(input_list) - 1
    mid =(len(input_list) - 1)// 2
    while not (input_list[mid] > input_list[mid -1] and input_list[mid] > input_list[mid +1]):
        if input_list[mid] > input_list[right]:
            left = mid
            mid = (left + right)//2
        elif input_list[mid] < input_list[right]:
            right = mid
            mid = (left + right) //2
    return mid


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


# Test cases:
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([[2], 0])
test_function([[2], 2])




