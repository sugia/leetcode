'''
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

Input:"-1/2+1/2"
Output: "0/1"

Example 2:

Input:"-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input:"1/3-1/2"
Output: "-1/6"

Example 4:

Input:"5/3+1/3"
Output: "2/1"

Note:

    The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
    The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
    The number of given fractions will be in the range [1,10].
    The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

'''

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        i = 0
        a = 0
        b = 1
        while i < len(expression):
            j = i+1
            while j < len(expression) and expression[j] not in '+-':
                j += 1
            tmp = expression[i:j]
            sign = 1
            if tmp[0] == '+':
                tmp = tmp[1:]
            elif tmp[0] == '-':
                tmp = tmp[1:]
                sign = -sign
            idx = 0
            while idx < len(tmp) and tmp[idx] != '/':
                idx += 1
            c = int(tmp[:idx]) * sign
            d = int(tmp[idx+1:])
            
            y = b * d
            x = d * a + b * c
            gcd = self.get(x, y)
            a, b = x // gcd, y // gcd
            
            
            i = j
        return str(a) + '/' + str(b)
    
    def get(self, a, b):
        if b == 0:
            return a
        else:
            return self.get(b, a%b)
