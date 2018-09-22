'''
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
'''

class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        
        dic = {}
        for i in xrange(len(dict)):
            k = self.getInitialKey(dict[i])
            if k in dic:
                dic[k].append(i)
            else:
                dic[k] = [i]
        
        flag = True
        while flag:
            flag = False
            kk = None
            for k, v in dic.iteritems():
                if len(v) > 1:
                    flag = True
                    kk = k
                    break
            if kk:
                vv = dic[kk]
                del dic[kk]
                for v in vv:
                    k = self.extendKey(dict[v], kk)
                    if k in dic:
                        dic[k].append(v)
                    else:
                        dic[k] = [v]
        
            
        res = ['' for i in xrange(len(dict))]
        for k, v in dic.iteritems():
            res[v[0]] = k
        return res
        
    def getInitialKey(self, key):
        if len(key) < 3:
            return key
        res = key[0] + str(len(key)-2) + key[-1]
        if len(res) < len(key):
            return res
        else:
            return key
        
    def extendKey(self, key, prev):
        idx = -1
        for i in xrange(len(prev)):
            if prev[i].isdigit():
                idx = i
                break
        if idx == -1:
            return key
        res = key[:idx+1] + str(len(key) - (idx + 2)) + key[-1]
        if len(res) < len(key):
            return res
        return key
