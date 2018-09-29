'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            raise 'error: denominator is zero'
        if numerator == 0:
            return '0'
        sign = 1
        if numerator < 0:
            sign = -sign
            numerator = -numerator
        if denominator < 0:
            sign = -sign
            denominator = -denominator
        
        res = ''
        if sign == -1:
            res += '-'
        res += str(numerator // denominator)
        remain = numerator % denominator
        if remain == 0:
            return res
        
        res += '.'
        f = {remain: len(res)}
        while True:
            val = remain * 10 // denominator
            remain = remain * 10 % denominator
            res += str(val)
            if remain == 0:
                return res
            if remain in f:
                return res[:f[remain]] + '(' + res[f[remain]:] + ')'
            f[remain] = len(res)
            
        
        
