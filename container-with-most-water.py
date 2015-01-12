class Solution:
    #given a list of integer
    #return an integer
    def maxArea(self, height):
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                res = max(res, height[left] * (right - left))
                left += 1
            else:
                res = max(res, height[right] * (right - left))
                right -= 1
        return res
