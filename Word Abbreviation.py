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
        # abbr: (i, word, first_dis_idx)
        dic = {}
        for i in xrange(len(dict)):
            abbr, idx = self.getAbbr(dict[i])
            if abbr in dic:
                dic[abbr].append((i, dict[i], idx))
            else:
                dic[abbr] = [(i, dict[i], idx)]
        
        while True:
            keys = []
            for key in dic:
                if len(dic[key]) > 1:
                    keys.append(key)
            if not keys:
                break
            for key in keys:
                vec = dic.pop(key)
                for i, word, idx in vec:
                    new_word, new_idx = self.extendAbbr(word, idx)
                    if new_word in dic:
                        dic[new_word].append((i, word, new_idx))
                    else:
                        dic[new_word] = [(i, word, new_idx)]
            
        res = ['' for i in xrange(len(dict))]
        for key in dic:
            i, word, idx = dic[key][0]
            res[i] = key
        return res
            
    def getAbbr(self, word):
        # return abbr, idx
        if len(word) < 4:
            return word, -1
        return word[0] + str(len(word)-2) + word[-1], 1
    
    def extendAbbr(self, word, idx):
        # return abbr, idx
        new_idx = idx + 1
        if new_idx >= len(word) - 2:
            return word, -1
        return word[:new_idx] + str(len(word) - (new_idx+1)) + word[-1], new_idx
