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
        s = s.replace(' ', '')
        return self.cal(s, 0)[0]
    
    def update(self, stack, op, tmp):
        if op == '+':
            stack.append(tmp)
        elif op == '-':
            stack.append(-tmp)
        elif op == '*':
            stack[-1] *= tmp
        elif op == '/':
            if stack[-1] >= 0:
                stack[-1] //= tmp
            else:
                stack[-1] = -(-stack[-1] // tmp)
            
    def cal(self, s, idx):
        stack = []
        op = '+'
        tmp = 0
        while idx < len(s):
            if s[idx].isdigit():
                tmp = tmp * 10 + int(s[idx])
                idx += 1
            elif s[idx] == '(':
                tmp, idx = self.cal(s, idx+1)
            elif s[idx] == ')':
                self.update(stack, op, tmp)
                return sum(stack), idx+1
            else:
                self.update(stack, op, tmp)
                op = s[idx]
                tmp = 0
                idx += 1
        self.update(stack, op, tmp)
        return sum(stack), idx
