'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]
        start.sort()
        end.sort()
        
        res = 0
        idx = 0
        for i in xrange(len(start)):
            if start[i] < end[idx]:
                res += 1
            else:
                idx += 1
                
        return res
