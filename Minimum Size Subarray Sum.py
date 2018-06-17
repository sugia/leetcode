'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        res = float('inf')
        tmp = 0
        
        while end < len(nums):
            tmp += nums[end]
            end += 1
                
            while tmp >= s:
                res = min(res, end - start)
                tmp -= nums[start]
                start += 1
                
        if res == float('inf'):
            return 0
        return res
