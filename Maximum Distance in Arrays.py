'''

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
'''

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
        
        if not arrays or len(arrays) < 2:
            return 0
        
        res = 0
        tmpmin = arrays[0][0]
        tmpmax = arrays[0][-1]
        
        for i in xrange(1, len(arrays)):
            res = max(res, abs(tmpmin - arrays[i][-1]), abs(tmpmax - arrays[i][0]))
            tmpmin = min(tmpmin, arrays[i][0])
            tmpmax = max(tmpmax, arrays[i][-1])
            
        return res
