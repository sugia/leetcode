'''
 Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.

Example 2:

Given s = "apple", abbr = "a2e":

Return false.

Seen this question in a real interview before?  

    Difficulty:Easy
    Total Accepted:16.8K
    Total Submissions:59.2K
    Contributor:LeetCode
    Companies 


Related Topics 

'''

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        while j < len(abbr) and i < len(word):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                
                tmp = 0
                while j < len(abbr) and abbr[j].isdigit():
                    tmp = tmp * 10 + int(abbr[j])
                    j += 1
                if i + tmp > len(word):
                    return False
                i += tmp
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                
        if i != len(word) or j != len(abbr):
            return False
        
        return True
