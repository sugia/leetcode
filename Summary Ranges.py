'''

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        nums.sort()
        res = []
        is_head = True
        
        for i in xrange(len(nums)):
            if is_head:
                res.append(str(nums[i]))
                is_head = False
            else:
                if nums[i] == nums[i-1] + 1:
                    if '->' not in res[-1]:
                        res[-1] += '->'
                    else:
                        res[-1] = res[-1][:res[-1].index('->') + 2]
                    res[-1] += str(nums[i])
                else:
                    res.append(str(nums[i]))
                    
        return res
