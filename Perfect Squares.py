'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        vec = [(n, 0)]
        visited = set()
        while vec:
            s, step = vec.pop(0)
            if s == 0:
                return step
            for i in reversed(xrange(int(math.sqrt(s)) + 1)):
                if s-i*i not in visited:
                    visited.add(s-i*i)
                    vec.append((s-i*i, step+1))
        return n
