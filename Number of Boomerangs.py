'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

import math

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0

        for i in xrange(len(points)):
            distance_count = {}
            for j in xrange(len(points)):
                if i == j:
                    continue
                distance = self.getDistance(points[i], points[j])
                
                if distance in distance_count:
                    distance_count[distance] += 1
                else:
                    distance_count[distance] = 1
               
            for distance in distance_count:
                res += distance_count[distance] * (distance_count[distance] - 1)
        
        return res
    
    def getDistance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
