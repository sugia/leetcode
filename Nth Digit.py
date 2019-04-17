'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        len(1): 0-9 = 10 * 1 = 10
        len(2): 10-99 = 90 * 2 = 180
        len(3): 100-999 = 900 * 3 = 2700
        '''
        if n < 10:
            return n
        n -= 10
        w = 2
        while n > 9 * 10 ** (w-1) * w:
            n -= 9 * 10 ** (w-1) * w
            w += 1
        
        num = 10 ** (w-1) + n // w
        step = n % w
        return int(str(num)[step])
        
