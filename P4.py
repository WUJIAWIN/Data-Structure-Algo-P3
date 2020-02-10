# Problem 4
# Dutch National Flag Problem
# Single traversal.

def sort_012(input_list):
    list = [1] * len(input_list)
    left = 0
    right = len(input_list)-1
    i = 0
    while i <= len(input_list)-1:
        if input_list[i] == 0:
            list[left] = 0
            left += 1
            i += 1
        elif input_list[i] == 2:
            list[right] = 2
            right -= 1
            i +=1
        else:
            i += 1
    return list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0])
test_function([])
test_function([1, 1, 1, 1, 1, 1])





