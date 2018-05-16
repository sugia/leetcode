'''

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        sign = 1
        if num < 0:
            sign = -1
            num = -num
            
        res = ''
        while num > 0:
            res = str(num % 7) + res
            num //= 7
            
        if sign < 0:
            res = '-' + res
            
        return res
        
        
