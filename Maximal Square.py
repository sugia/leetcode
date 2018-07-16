'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4


'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        
        res = 0
        dp = [[0 for j in xrange(m)] for i in xrange(n)]
        
        for i in xrange(n):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                res = max(res, dp[i][0])
                
        for j in xrange(m):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                res = max(res, dp[0][j])
                
        for i in xrange(1, n):
            for j in xrange(1, m):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    res = max(res, dp[i][j])
                    
        return res * res
