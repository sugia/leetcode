'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = [0 for i in xrange(len(nums))]
        nums_idx = 0
        res_idx = 0
        while res_idx < len(res):
            res[res_idx] = nums[nums_idx]
            res_idx += 2
            nums_idx += 1
        res_idx = 1
        while res_idx < len(res):
            res[res_idx] = nums[nums_idx]
            res_idx += 2
            nums_idx += 1
            
        for i in xrange(len(res) - 1):
            if res[i] == res[i+1]:
                res = res[i+1:] + res[:i+1]
                break
        
        nums[:] = res[:]

        
