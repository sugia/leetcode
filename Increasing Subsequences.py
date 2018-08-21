'''
 Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:

    The length of the given array will not exceed 15.
    The range of integer in the given array is [-100,100].
    The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

'''

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        box = set()
        box.add(())
        for x in nums:
            more = set()
            for tmp in box:
                if not tmp or tmp[-1] <= x:
                    more.add(tmp + (x,))
            box |= more
        res = []
        for x in box:
            if len(x) > 1:
                res.append(list(x))
        return res
            
