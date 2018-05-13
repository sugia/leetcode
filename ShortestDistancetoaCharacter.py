'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''

import sys

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        shortest_from_left = [sys.maxint for i in xrange(len(S))]
        for i in xrange(len(S)):
            if S[i] == C:
                shortest_from_left[i] = 0
            else:
                if i == 0 or shortest_from_left[i - 1] == sys.maxint:
                    shortest_from_left[i] = sys.maxint
                else:
                    shortest_from_left[i] = shortest_from_left[i - 1] + 1
        
        shortest_from_right = [sys.maxint for i in xrange(len(S))]
        for i in reversed(xrange(len(S))):
            if S[i] == C:
                shortest_from_right[i] = 0
            else:
                if i == len(S) - 1 or shortest_from_right[i + 1] == sys.maxint:
                    shortest_from_right[i] = sys.maxint
                else:
                    shortest_from_right[i] = shortest_from_right[i + 1] + 1
        
        res = []
        for i in xrange(len(S)):
            res.append(min(shortest_from_left[i], shortest_from_right[i]))
        
        return res
