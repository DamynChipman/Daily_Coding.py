"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

# ===== Test cases =====
test_mat1 = [[10, 12, 14, 16, 18, 20],
             [12, 14, 7, 7, 20, 22],
             [14, 18, 20, 8, 8, 5],
             [13, 14, 17, 18, 6, 6]]

# ===== Solution =====
import numpy as np
def minCost(mat):

    # Attempt 1
    cur_min = mat[0][0]
    for row in mat:
        for i in np.arange(0,len(row)):
            if row[i] < cur_min:
                if i == 0 and row[i] != row[i+1]:
                    cur_min = row[i]
                elif i == len(row)-1 and row[i] != row[i-1]:
                    cur_min = row[i]
                else:
                    if row[i] != row[i+1] and row[i] != row[i-1]:
                        cur_min = row[i]

    return cur_min

# ===== Testing =====
print(test_mat1)
print(minCost(test_mat1))
