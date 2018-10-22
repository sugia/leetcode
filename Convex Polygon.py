'''
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

 

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
 

Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:
Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:

'''


class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points = points + [points[0], points[1]]
        sign = 0
        for i in xrange(len(points)-2):
            if sign == 0:
                sign = self.cal(self.sub(points[i+2], points[i+1]), self.sub(points[i+1], points[i]))
                # print 'sign', sign
            else:
                new_sign = self.cal(self.sub(points[i+2], points[i+1]), self.sub(points[i+1], points[i]))
                # print 'new_sign', new_sign
                if new_sign != 0 and new_sign != sign:
                    return False
        
        return True
    
    def cal(self, a, b):
        tmp = a[1] * b[0] - a[0] * b[1]
        if tmp == 0:
            return 0
        elif tmp > 0:
            return 1
        else:
            return -1
        
    def sub(self, a, b):
        return [a[0] - b[0], a[1] - b[1]]
