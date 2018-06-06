'''
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
'''

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row_sum = [0 for i in xrange(len(grid))]
        col_sum = [0 for j in xrange(len(grid[0]))]
        
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                row_sum[i] += grid[i][j]
                col_sum[j] += grid[i][j]
                
        res = 0
        res += self.getSum(row_sum)
        res += self.getSum(col_sum)
        
        return res
    
    def getSum(self, vec):
        tmp_left = [0 for i in xrange(len(vec))]
        acc_left = [0 for i in xrange(len(vec))]
        acc_left[0] = vec[0]
        
        for i in xrange(1, len(vec)):
            tmp_left[i] = tmp_left[i-1] + acc_left[i-1]
            acc_left[i] = acc_left[i-1] + vec[i]
            
        tmp_right = [0 for i in xrange(len(vec))]
        acc_right = [0 for i in xrange(len(vec))]
        acc_right[-1] = vec[-1]
        for i in reversed(xrange(len(vec) - 1)):
            tmp_right[i] = tmp_right[i+1] + acc_right[i+1]
            acc_right[i] = acc_right[i+1] + vec[i]
            
        idx = 0
        for i in xrange(len(vec)):
            if tmp_left[i] + tmp_right[i] < tmp_left[idx] + tmp_right[idx]:
                idx = i
        

        return tmp_left[idx] + tmp_right[idx]
        
