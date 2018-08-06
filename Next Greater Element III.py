'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21

 

Example 2:

Input: 21
Output: -1

'''

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        vec = [int(x) for x in list(str(n))]
        
        idx = -1
        for i in reversed(xrange(len(vec) - 1)):
            if vec[i] < vec[i+1]:
                idx = i
                break
                
        if idx == -1:
            return -1
        
        for i in reversed(xrange(idx+1, len(vec))):
            if vec[i] > vec[idx]:
                vec[i], vec[idx] = vec[idx], vec[i]
                vec[idx+1:] = vec[idx+1:][::-1]
                res = int(''.join([str(x) for x in vec]))
                if res > 2147483647:
                    return -1
                else:
                    return res
        return -1
