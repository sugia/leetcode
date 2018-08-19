'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:

11000
11000
00011
00011

Given the above grid map, return 1.

Example 2:

11011
10000
00001
11011

Given the above grid map, return 3.

Notice that:

11
1

and

 1
11

are considered different island shapes, because we do not consider reflection / rotation.

Note: The length of each dimension in the given grid does not exceed 50. 
'''

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        box = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 1:
                    self.get(grid, i, j, box)
                    
        return len(box)
    
    def get(self, grid, x, y, box):
        tmp = [(0, 0)]
        grid[x][y] = 0
        
        vec = [(x, y)]
        while vec:
            a, b = vec.pop()
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                aa, bb = a + i, b + j
                if 0 <= aa < len(grid) and 0 <= bb < len(grid[0]):
                    if grid[aa][bb] == 1:
                        grid[aa][bb] = 0
                        tmp.append((aa - x, bb - y))
                        vec.append((aa, bb))
        tmp.sort()
        box.add(tuple(tmp))
