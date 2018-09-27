'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

 

Note: Do not use the eval built-in library function.

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
            stack[-1] = stack[-1] // tmp
        
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
