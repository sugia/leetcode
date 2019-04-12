'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        step = 1
        while step <= n:
            prefix = n // step
            digit = prefix % 10
            prefix //= 10
            suffix = n % step
            
            if digit == 0:
                res += prefix * step
            elif digit == 1:
                res += prefix * step
                res += suffix + 1
            else:
                res += (prefix + 1) * step
                
            step *= 10
            
        return res
