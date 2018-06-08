'''

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fre = {}
        for num in nums:
            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1
                
        res = []
        for key in fre:
            if fre[key] == 1:
                res.append(key)
                
        return res
