"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

# ===== Test cases =====
def f1(x):
    print(x)
    return 0

def f2(x1,x2):
    print(x1)
    print(x2)
    return 0


# ===== Solution =====
import time
def jobScheduler(f,args,n):
    time.sleep(n)
    return f(args)

# ===== Testing =====
jobScheduler(f1,'hello',2)
jobScheduler(f1,['hello','there'],2)
