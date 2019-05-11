"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

# ===== Test cases =====
test1 = [6, 1, 3, 3, 3, 6, 6]
test2 = [13, 19, 13, 13]
test3 = [2, 6, 3, 7, 7, 6, 7, 6, 3, 3]

# ===== Solution =====
def oneOfThree(list):
    counter = [list[0]]

    for value in list:
        
