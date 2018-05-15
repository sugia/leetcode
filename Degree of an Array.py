'''

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_idx = {}
        right_idx = {}
        frequency = {}
        
        res = []
        top_frequency = -1
        
        for i in xrange(len(nums)):
            if nums[i] not in left_idx:
                left_idx[nums[i]] = i
            right_idx[nums[i]] = i
            
            if nums[i] not in frequency:
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] += 1
                
            if frequency[nums[i]] > top_frequency:
                res = [nums[i]]
                top_frequency = frequency[nums[i]]
                
            elif frequency[nums[i]] == top_frequency:
                res.append(nums[i])

        ans = float('inf')
        for r in res:
            ans = min(ans, right_idx[r] - left_idx[r] + 1)
            
        return ans
                
