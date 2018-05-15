'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_to_fre = {}
        for c in magazine:
            if c in char_to_fre:
                char_to_fre[c] += 1
            else:
                char_to_fre[c] = 1
                
        for c in ransomNote:
            if c in char_to_fre:
                char_to_fre[c] -= 1
            else:
                char_to_fre[c] = -1
                
        for c in ransomNote:
            if char_to_fre[c] < 0:
                return False
            
        return True
