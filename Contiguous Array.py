'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000. 
'''

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dic = {0: -1}
        
        res = 0
        tmp = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                tmp -= 1
            else:
                tmp += 1
            
            if tmp in dic:
                res = max(res, i - dic[tmp])
            else:
                dic[tmp] = i
                
        return res
