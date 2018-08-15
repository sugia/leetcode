'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dic = {}
        res = []
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                tmp = nums[i] + nums[j]
                
                if target - tmp in dic:
                    for (x, y) in dic[target - tmp]:
                        if i != x and i != y and j != x and j != y:
                            candidate = sorted([nums[i], nums[j], nums[x], nums[y]])
                            if candidate not in res:
                                res.append(candidate)
                if tmp in dic:
                    dic[tmp].add((i, j))
                else:
                    dic[tmp] = set([(i, j)])
        return res
        
                    
                    
        
