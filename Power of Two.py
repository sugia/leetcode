'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Example 2:

Input: 16
Output: true
Example 3:

Input: 218
Output: false
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        bit_count = 0
        while n > 0:
            bit_count += n & 1
            n >>= 1
            
        if bit_count == 1:
            return True
        return False
