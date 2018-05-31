'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        if rowIndex == 0:
            return res
        for i in xrange(1, rowIndex + 1):
            next_res = [1]
            for j in xrange(1, i):
                next_res.append(res[j-1] + res[j])
            next_res.append(1)
            
            res = next_res
        return res
