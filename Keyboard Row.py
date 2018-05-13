'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        str_in_row = {}
        str_in_row[0] = 'qwertyuiop'
        str_in_row[1] = 'asdfghjkl'
        str_in_row[2] = 'zxcvbnm'
        char_to_row = {}
        for row in str_in_row:
            for c in str_in_row[row]:
                char_to_row[c] = row
                char_to_row[c.upper()] = row
                
        res = []
        for word in words:
            box = set()
            for c in word:
                box.add(char_to_row[c])
            if len(box) < 2:
                res.append(word)
        
        return res
        
