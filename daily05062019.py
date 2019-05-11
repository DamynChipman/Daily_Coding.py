"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

# ===== Solution =====
class Stack:

    _containter = []
    _size = 0
    _max = 0

    def __init__(self):
        self._containter = []
        self._max = 0
        self._size = 0

        return None

    def push(self, val):
        self._containter.append(val)
        self._size += 1
        if val > self._max:
            self._max = val
        return True

    def pop(self):
        self._size -= 1
        return self._containter.pop()

    def max(self):
        if self._size == 0:
            return None
        return self._max

    def to_string(self):
        to_return = ''
        for item in self._containter:
            to_return += str(item) + ' '
        return to_return

# ===== Debugging =====
stack = Stack()
stack.push(3)
stack.push(4)
print(stack.to_string())
print(stack.max())
stack.push(2)
stack.push(6)
stack.push(2)
stack.push(4)
stack.push(1)
print(stack.to_string())
stack.pop()
print(stack.to_string())
stack.pop()
print(stack.to_string())
stack.pop()
print(stack.to_string())
