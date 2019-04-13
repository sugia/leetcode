'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        f = {i: [nums[i]] for i in range(len(nums))}
        res = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(f[i]) < len(f[j]) + 1:
                    f[i] = f[j] + [nums[i]]
                
            if len(res) < len(f[i]):
                res = f[i]
        return res
                    
