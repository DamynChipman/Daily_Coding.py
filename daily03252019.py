"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# ===== Test cases =====
test_list1 = [10, 15, 3, 7]
test_list2 = [1, 2, 3, 4, 5]
test_list3 = []
test_list4 = [-13, -13, 2, 4, 10, 10]

test_value1 = 25
test_value2 = 13
test_value3 = 9
test_value4 = -26

# ===== Function =====
def checkList(list, value):
    """
    Given a list [x1, x2, ...] and value X, checks whether any two values of list
    add together to equal value.
    """

    # Attempt 1
    res = False
    for value1 in list:
        for value2 in list:
            if (value1 + value2) == value:
                res = True

    return res


# ===== Testing =====
if checkList(test_list4, test_value4):
    print('True!')
else:
    print('False!')
