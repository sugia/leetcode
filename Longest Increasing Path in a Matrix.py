'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]:
            return 0
        h = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                heapq.heappush(h, (matrix[i][j], i, j))
                
        f = [[1 for j in xrange(len(matrix[i]))] for i in xrange(len(matrix))]
        res = 1
        while h:
            _, x, y = heapq.heappop(h)
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xx, yy = x+i, y+j
                if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[0]):
                    if matrix[xx][yy] > matrix[x][y]:
                        f[xx][yy] = max(f[xx][yy], f[x][y] + 1)
                        res = max(res, f[xx][yy])
        return res
