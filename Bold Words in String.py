'''
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
'''

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        pairs = []
        for word in words:
            idx = S.find(word)
            while idx != -1:
                pairs.append([idx, idx + len(word)])
                idx = S.find(word, idx+1)
                
        pairs.sort(key = lambda x : (x[0], x[1]))
        
        res = []
        for pair in pairs:
            if not res:
                res.append(pair)
            else:
                if pair[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], pair[1])
                else:
                    res.append(pair)
                    
        for i in reversed(xrange(len(res))):
            S = S[:res[i][1]] + '</b>' + S[res[i][1]:]
            S = S[:res[i][0]] + '<b>' + S[res[i][0]:]
            
            
        return S
