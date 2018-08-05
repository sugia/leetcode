'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true

Example 2:

Input:  "88"
Output: true

Example 3:

Input:  "962"
Output: false


'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        '''
        1 2 3 4 5 6 7 8 9 0
        1 = 1
        6 = 9
        8 = 8
        9 = 6
        0 = 0
        '''
        
        pairs = {1:1, 6:9, 8:8, 9:6, 0:0}
        
        i = 0
        j = len(num) - 1
        while i <= j:
            if int(num[i]) not in pairs or int(num[j]) not in pairs or int(num[i]) != pairs[int(num[j])]:
                return False
            i += 1
            j -= 1
        
        return True
