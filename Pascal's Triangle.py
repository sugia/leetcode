'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        
        for i in xrange(1, numRows):
            row = [1]
            for j in xrange(1, i):
                row.append(res[-1][j-1] + res[-1][j])
            
            row.append(1)
            res.append(row)
        return res
