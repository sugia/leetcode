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
        
        rows, cols = self.getRowsCols(grid)
        return self.getDis(rows, rows[len(rows) // 2]) + self.getDis(cols, cols[len(cols) // 2])
        
    def getRowsCols(self, grid):
        rows = []
        cols = []
        for r in xrange(len(grid)):
            for c in xrange(len(grid[r])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)
        return sorted(rows), sorted(cols)
    
    def getDis(self, points, median):
        res = 0
        for p in points:
            res += abs(p - median)
        return res
    
        
