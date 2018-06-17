'''
You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4


'''

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[i])):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)
                    
    def bfs(self, rooms, original_x, original_y):
        vec = [(original_x, original_y)]
        
        while len(vec) > 0:
            (x, y) = vec.pop()
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + i, y + j
                if 0 <= new_x <len(rooms) and 0 <= new_y < len(rooms[new_x]):
                    if rooms[new_x][new_y] > rooms[x][y] + 1:
                        rooms[new_x][new_y] = rooms[x][y] + 1
                        vec.append((new_x, new_y))
                        
        
