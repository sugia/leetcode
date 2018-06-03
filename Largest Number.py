'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
                
        res = [str(x) for x in nums]
        
        while len(res) > 1 and res[0] == '0':
            res.pop(0)

        return ''.join(res)
