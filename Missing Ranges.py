'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        start = lower
        res = []
        for x in nums:
            if x == start:
                start = x + 1
            else:
                if x == start + 1:
                    res.append(str(start))
                elif start < x-1:
                    res.append(str(start) + '->' + str(x-1))
                start = x + 1
        
        if start == upper:
            res.append(str(start))
        elif start < upper:
            res.append(str(start) + '->' + str(upper))
        return res
