"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

# ===== Solution =====
class Log:

    def __init__(self):
        self._stack = []
        self._size = 0


    def record(self, order_id):
        self._stack.append(order_id)
        self._size += 1
        return True

    def get_last(self, i):
        return self._stack[i]

# ===== Testing =====
log = Log()
log.record(1)
log.record(2)
log.record(3)
log.record(4)
print(log.get_last(2))
