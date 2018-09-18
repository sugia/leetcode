'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.

'''

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        
        vec = sorted([self.dis(p1, p2), self.dis(p1, p3), self.dis(p1, p4), self.dis(p2, p3), self.dis(p2, p4), self.dis(p3, p4)])
        if vec[0] == vec[1] == vec[2] == vec[3] and vec[4] == vec[5] and vec[0] * 2 == vec[4]:
            return True
        return False
        
        
    def dis(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
