'''
 Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int. 
'''

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = [1 for i in xrange(len(nums))]
        c = [1 for i in xrange(len(nums))]
        max_l = 1
        
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    if l[j] + 1 < l[i]:
                        pass
                    elif l[j] + 1 == l[i]:
                        c[i] += c[j]
                    else:
                        l[i] = l[j] + 1
                        c[i] = c[j]
            
            max_l = max(max_l, l[i])
                
        res = 0
        for i in xrange(len(nums)):
            if l[i] == max_l:
                res += c[i]
                
        return res
        
        
