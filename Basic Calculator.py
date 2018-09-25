'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        signs = [1, 1]
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                i += 1
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += signs.pop() * int(s[start:i])
            elif s[i] == '+':
                signs.append(signs[-1])
                i += 1
            elif s[i] == '-':
                signs.append(-signs[-1])
                i += 1
            elif s[i] == '(':
                signs.append(signs[-1])
                i += 1
            elif s[i] == ')':
                signs.pop()
                i += 1
            else:
                i += 1
        return res
