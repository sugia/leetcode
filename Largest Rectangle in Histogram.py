'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10


'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        i = 0
        while i <= len(heights):
            if not stack or (i < len(heights) and heights[stack[-1]] < heights[i]):
                stack.append(i)
                i += 1
            else:
                last = stack.pop()
                if stack:
                    res = max(res, heights[last] * (i - stack[-1] - 1))
                else:
                    res = max(res, heights[last] * i)
                    
        return res
