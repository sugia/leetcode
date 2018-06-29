'''
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.

Follow up:
If this function is called many times, how would you optimize it?

'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        data = [0 for i in xrange(32)]
        for i in xrange(32):
            data[i] = n & 1
            n >>= 1
            
        step = 1
        res = 0
        for i in reversed(xrange(32)):
            res += data[i] * step
            step *= 2
            
        return res
