'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        threshold = len(nums) // 3
        fre = {}
        res = set()
        for num in nums:
            if num in fre:
                fre[num] += 1

            else:
                fre[num] = 1
            
            if fre[num] > threshold:
                res.add(num)
                
        return list(res)
