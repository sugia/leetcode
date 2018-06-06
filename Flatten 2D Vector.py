'''
Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
Output: [1,2,3,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,2,3,4,5,6].
'''

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.x = 0
        self.y = -1
        self.vec2d = vec2d

    def next(self):
        """
        :rtype: int
        """
        return self.vec2d[self.x][self.y]

    def hasNext(self):
        """
        :rtype: bool
        """
        self.y += 1
        while self.x < len(self.vec2d) and self.y >= len(self.vec2d[self.x]):
            self.y = 0
            self.x += 1
        
        return self.x < len(self.vec2d)
    
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
