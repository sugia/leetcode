'''
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.

Example 1:

Input: "()"
Output: True

Example 2:

Input: "(*)"
Output: True

Example 3:

Input: "(*))"
Output: True

Note:

    The string size will be in the range [1, 100].

'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmax = 0
        cmin = 0
        for c in s:
            if c == '(':
                cmax += 1
                cmin += 1
            elif c == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            elif c == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            else:
                return False
            if cmax < 0:
                return False
        return cmin == 0
