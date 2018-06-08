'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        big = nums[0]
        small = nums[0]
        
        for i in xrange(1, len(nums)):
            big, small = max(nums[i], nums[i] * big, nums[i] * small), min(nums[i], nums[i] * big, nums[i] * small)
            res = max(res, big)
        return res
