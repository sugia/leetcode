'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''

import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        '''
        points.sort(key = lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
        return points[:K]
        '''
        
        idx = self.partition(points)
        if idx + 1 == K:
            return points[:K]
        elif idx + 1 < K:
            return points[:idx+1] + self.kClosest(points[idx+1:], K - (idx + 1))
        else:
            return self.kClosest(points[:idx], K)
        
    def partition(self, points):
        idx = 0
        for i in xrange(len(points)):
            if points[i][0] ** 2 + points[i][1] ** 2 < points[-1][0] ** 2 + points[-1][1] ** 2:
                points[i], points[idx] = points[idx], points[i]
                idx += 1
        points[-1], points[idx] = points[idx], points[-1]
        return idx
