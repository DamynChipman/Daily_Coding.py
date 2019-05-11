"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

# ===== Test Cases =====
TC1 = [2,4,6,2,5]
TC2 = [5,1,1,5]
TC3 = []
TC4 = [-2,0,3,4,-3]

# ===== Solution =====
def largestSum(list):

    # Attempt 1

    sum = 0
    for i in np.arange(0,len(list)):
        sum = value +

    return sum

# ===== Testing =====
print('TC1: '+str(TC1))
print(largestSum(TC1))
