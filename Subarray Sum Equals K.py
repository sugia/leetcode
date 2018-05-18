'''

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        box = {0:1}
        tmp = 0
        res = 0
        for num in nums:
            tmp += num
            if tmp - k in box:
                res += box[tmp - k]
            if tmp in box:
                box[tmp] += 1
            else:
                box[tmp] = 1
                
                
        return res
