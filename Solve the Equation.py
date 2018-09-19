'''
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
'''

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        equal_idx = equation.index('=')
        if equal_idx == -1:
            return 'Infinite solution'
        left = self.get(equation[:equal_idx])
        right = self.get(equation[equal_idx+1:])
        
        variable = []
        constant = []
        for x in left:
            if 'x' in x:
                variable.append(x)
            else:
                constant.append(self.neg(x))
        for x in right:
            if 'x' in x:
                variable.append(self.neg(x))
            else:
                constant.append(x)
        
        v = self.solve(variable)
        c = self.solve(constant)
        
        if v == '0':
            if c == '0':
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            a = v[:-1]
            if a:
                a = int(a)
            else:
                a = 1
            return 'x=' + str(int(c) // a)
        
    def get(self, s):
        vec = []
        start = 0
        for end in xrange(1, len(s)):
            if s[end] in '+-':
                vec.append(s[start:end])
                start = end
        vec.append(s[start:])
        return vec
    
    def neg(self, x):
        if x[0] == '+':
            return '-' + x[1:]
        if x[0] == '-':
            return x[1:]
        return '-' + x
    
    def solve(self, vec):
        if not vec:
            return '0'
        res = 0
        sign = False
        if 'x' in vec[0]:
            sign = True
        for x in vec:
            if x[-1] == 'x':
                y = x[:-1]
                if y == '' or y == '+':
                    y = 1
                elif y == '-':
                    y = -1
                else:
                    y = int(x[:-1])
                res += y
            else:
                res += int(x)
        if sign:
            if res == 0:
                return '0'
            elif res == 1:
                return 'x'
            else:
                return str(res) + 'x'
        else:
            return str(res)
    
        
