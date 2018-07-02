'''
There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.

Example 1:

Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:

Note:

    All given positions won't overlap.
    The squirrel can take at most one nut at one time.
    The given positions of nuts have no order.
    Height and width are positive integers. 3 <= height * width <= 10,000.
    The given positions contain at least one nut, only one tree and one squirrel.

'''

class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        dis = []
        for x, y in nuts:
            dis.append(abs(x - tree[0]) + abs(y - tree[1]))
            
        total = sum(dis) * 2
        
        res = float('inf')
        for i in xrange(len(nuts)):
            res = min(res, abs(nuts[i][0] - squirrel[0]) + abs(nuts[i][1] - squirrel[1]) - dis[i] + total)
            
        return res
