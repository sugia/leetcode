'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
'''

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        res = (D - B) * (C - A) + (H - F) * (G - E)
        
        x1 = max(A, E)
        y1 = max(B, F)
        
        x2 = min(C, G)
        y2 = min(D, H)
        
        if x1 <= x2 and y1 <= y2:
            res -= (x2 - x1) * (y2 - y1)
        
        return res
