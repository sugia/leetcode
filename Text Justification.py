'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


'''


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        idx = 0
        while idx < len(words):
            tmp = [words[idx]]
            space = maxWidth - len(words[idx])
            idx += 1
            while idx < len(words) and space >= len(words[idx]) + 1:
                tmp.append(words[idx])
                space -= 1 + len(words[idx])
                idx += 1
            
            slot = len(tmp) - 1
            space += slot
            
            if idx != len(words):
                # not last line
                row = tmp[-1]
                for i in reversed(xrange(len(tmp) - 1)):
                    count = space // slot
                    row = ' ' * count + row
                    space -= count
                    slot -= 1

                    row = tmp[i] + row
            else:
                # last line should be left adjusted
                row = ' '.join(tmp)
                space = maxWidth - len(row)
            row += ' ' * space
            res.append(row)
            
        return res
                
            
            
