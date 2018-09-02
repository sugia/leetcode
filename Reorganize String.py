'''

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dic = {}
        for c in S:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        maxf = max(dic.values())
        if maxf * 2 - 1 > len(S):
            return ''
        res = ['' for i in xrange(len(S))]
        idx = 0
        vec = sorted([(k, v) for k, v in dic.iteritems()], key = lambda x: (x[1], x[0]), reverse=True)
        for k, v in vec:
            for i in xrange(v):
                res[idx] = k
                idx += 2
                if idx >= len(res):
                    idx = 1
        return ''.join(res)
        
        
        
