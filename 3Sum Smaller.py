'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]

Follow up: Could you solve it in O(n2) runtime?

'''

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                k = len(nums) - 1
                while j < k and nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                res += k - j
        
        return res
