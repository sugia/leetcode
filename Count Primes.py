'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        res = [1 for i in xrange(n)]
        res[0] = 0
        res[1] = 0
        for i in xrange(2, n):
            if res[i] == 0:
                continue
            j = i
            while j + i < n:
                res[j+i] = 0
                j += i
                
        return sum(res)
