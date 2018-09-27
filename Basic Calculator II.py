'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

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
            stack[-1] = stack[-1] * tmp
        elif op == '/':
            if stack[-1] >= 0:
                stack[-1] //= tmp
            else:
                stack[-1] = -(-stack[-1] // tmp)
        
    def cal(self, s, idx):
        '''
        s: str
        idx: int
        rtype: (sum, idx)
        '''
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
