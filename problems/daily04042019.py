"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

# ===== Test cases =====
test_query1 = 'de'
test_set1 = ['dog', 'deer', 'deal']
test_query2 = 'app'
test_set2 = ['apple', 'application', 'app', 'beta']
test_query3 = ''
test_set3 = []
test_query4 = ''
test_set4 = ['asdf', 'qwer']

# ===== Solution =====
def autoComplete(query, set):

    # Attempt 1
    lQ = len(query)
    to_return = []
    for word in set:
        if query == word[0:lQ] and lQ != 0:
            to_return.append(word)

    return to_return

# ===== Testing =====
print('query: '+test_query4)
print('set: '+str(test_set4))
print('res: '+str(autoComplete(test_query4,test_set4)))
