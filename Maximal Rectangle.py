'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6


'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        h = [0 for i in xrange(len(matrix[0]))]
        for row in matrix:
            for i in xrange(len(row)):
                if row[i] == '1':
                    h[i] += 1
                else:
                    h[i] = 0
                
            stack = []
            i = 0
            while i <= len(h):
                if not stack or (i < len(h) and h[stack[-1]] < h[i]):
                    stack.append(i)
                    i += 1
                else:
                    last = stack.pop()
                    if stack:
                        res = max(res, h[last] * (i - stack[-1] - 1))
                    else:
                        res = max(res, h[last] * i)
                
        return res
