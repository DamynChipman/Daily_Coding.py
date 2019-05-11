"""
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

# ===== Solution =====
from random import *

def rand5():
    return randint(1,5)

def rand7():
    return (rand5() + rand5()) % 7 + 1

# ===== Debugging =====
for i in range(10):
    print(rand7())
