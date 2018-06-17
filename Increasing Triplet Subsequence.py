'''
 Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        
        min_from_left = [0 for i in xrange(len(nums))]
        min_from_left[0] = nums[0]
        
        for i in xrange(1, len(nums)):
            min_from_left[i] = min(min_from_left[i-1], nums[i])
            
            
        max_from_right = [0 for i in xrange(len(nums))]
        max_from_right[-1] = nums[-1]
        
        for i in reversed(xrange(len(nums) - 1)):
            max_from_right[i] = max(max_from_right[i+1], nums[i])
            
            
            
        for i in xrange(1, len(nums) - 1):
            if min_from_left[i] < nums[i] < max_from_right[i]:
                return True
            
        return False
