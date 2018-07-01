'''
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:

Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.

Note:

    The range of width and height of the input 2D array is [1,500].

'''

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        
        if not picture:
            return 0
        row_b = [0 for i in xrange(len(picture))]
        col_b = [0 for j in xrange(len(picture[0]))]
        
        for i in xrange(len(picture)):
            for j in xrange(len(picture[i])):
                if picture[i][j] == 'B':
                    row_b[i] += 1
                    col_b[j] += 1
                    
        res = 0
        for i in xrange(len(picture)):
            for j in xrange(len(picture[i])):
                if picture[i][j] == 'B' and row_b[i] == 1 and col_b[j] == 1:
                    res += 1
        
        return res
