'''
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.

Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.

Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.


'''

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        h = []
        for key, value in dic.iteritems():
            heapq.heappush(h, (-value, key))
        
        res = []
        last_idx = {}
        for _ in xrange(len(s)):
            modified = False
            vec = []
            while h:
                neg_value, key = heapq.heappop(h)
                if key not in last_idx or len(res) - last_idx[key] >= k:
                    last_idx[key] = len(res)
                    res.append(key)
                    
                    if neg_value + 1 < 0:
                        vec.append((neg_value + 1, key))
                    modified = True
                    break
                else:
                    vec.append((neg_value, key))
            
            if not modified:
                return ''
            for item in vec:
                heapq.heappush(h, item)
        
        return ''.join(res)
        
        
