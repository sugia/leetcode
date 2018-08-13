'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

    Each 0 marks an empty land which you can pass by freely.
    Each 1 marks a building which you cannot pass through.
    Each 2 marks an obstacle which you cannot pass through.

Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

'''

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dis = [[0 for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        step = [[0 for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        tot = 0
        
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 1:
                    self.find(grid, i, j, dis, step, tot)
                    tot += 1
                    
        res = -1
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if step[i][j] == tot and grid[i][j] == 0 and (res == -1 or dis[i][j] < res):
                    res = dis[i][j]
        
        return res
    
    def find(self, grid, x, y, dis, step, tot):
        visited = [[False for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        vec = [(x, y)]
        visited[x][y] = True
        
        tmp = 0
        while vec:
            next_vec = []
            tmp += 1
            for a, b in vec:
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    aa = a + i
                    bb = b + j
                    if 0 <= aa < len(grid) and 0 <= bb < len(grid[0]):
                        if grid[aa][bb] == 0 and not visited[aa][bb] and step[aa][bb] == tot:
                            visited[aa][bb] = True
                            dis[aa][bb] += tmp
                            step[aa][bb] += 1
                            next_vec.append((aa, bb))

            vec = next_vec
                        
    
        
                    
