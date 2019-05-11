"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

# ===== Test Cases =====
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

test1 = cons(3,4)
test2 = cons('a','c')
test3 = cons('var','foo')
test4 = cons(23.4,'numb')

# ===== Solution =====
def extract1(a,b):
    return a

def extract2(a,b):
    return b

def car(pair):
    return pair(extract1)

def cdr(pair):
    return pair(extract2)

# ===== Tests =====
print(car(test4))
print(cdr(test4))
