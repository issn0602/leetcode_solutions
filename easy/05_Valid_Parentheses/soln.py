"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.

"""

def isValid(s):
    if len(s) == 0:
        return False
    valid = { '(' : ')', '{' : '}', '[' : ']' }
    stack = []
    flag = True
    i=0
    for i in s:
        if i in valid:
            stack.append(i)
        elif len(stack) == 0 or valid[stack.pop()] != i:
            return False
    return len(stack) == 0