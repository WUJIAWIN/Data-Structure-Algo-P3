# Problem 1
# Square Root of an Integer
# Expected time complexity is O(log(n))

def sqrt(number):
    if number < 0:
        return print("Negative number does not have a square root.")

    mid = number/2
    left = 0
    right = number
    while mid * mid != number:
        if mid * mid > number:
            left = left
            right = mid
            mid = (left + right)/2

        if mid * mid < number:
            left = mid
            right = right
            mid = (left + right)/2

    return int(mid)

# Test Case
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(-20)) else "Fail")



