'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import fractions

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
        if len(points) == 1:
            return 1
        
        # pairs (k, b), if k not exists, then k = float('inf')
        box = set()
        for i in xrange(len(points) + 1):
            for j in xrange(i + 1, len(points)):
                if points[i].x == points[j].x:
                    pair = (0, 0, points[i].x)
                else:
                    a = points[i].y - points[j].y
                    b = points[i].x - points[j].x
                    gcd = fractions.gcd(a, b)
                    a //= gcd
                    b //= gcd
                    c = points[i].y * b - a * points[i].x
                    pair = (a, b, c)

                if pair not in box:
                    box.add(pair)
                
        res = 0
        for (a, b, c) in box:
            tmp = 0
            for point in points:
                if a == 0 and b == 0 and point.x == c or b != 0 and c == point.y * b - a * point.x:
                    tmp += 1
            res = max(res, tmp)
        

        return res
