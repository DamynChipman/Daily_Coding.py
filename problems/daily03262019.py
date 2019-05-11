"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# ===== Test Cases =====
test_in1 = [1, 2, 3, 4, 5]
test_out1 = [120, 60, 40, 30, 24]
test_in2 = [3, 2, 1]
test_out2 = [2, 3, 6]

# ===== Solution =====
import numpy as np
def productArray(list):

    res = list

    # Attempt 1
    for i in np.arange(0,len(list)):
        product = 1
        for j in np.arange(0,len(list)):
            if i != j:
                product *= list[j]
        res[i] = product

    return res

# ===== Testing =====
print('Test case 1: '+str(test_in1))
print('Output: '+str(productArray(test_in1)))

print('Test case 2: '+str(test_in2))
print('Output: '+str(productArray(test_in2)))
