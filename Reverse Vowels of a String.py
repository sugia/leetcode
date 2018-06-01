'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vec = list(s)
        idx = []
        vowels = []
        for i in xrange(len(vec)):
            if vec[i] in set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                idx.append(i)
                vowels.append(vec[i])
        

        vowels = vowels[::-1]
        
        for i in xrange(len(idx)):
            vec[idx[i]] = vowels[i]
            
        return ''.join(vec)
