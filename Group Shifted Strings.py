'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            key = self.getKey(s)
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]

        return dic.values()
    
    def getKey(self, s):
        vec = [ord(c) for c in s]
        tmp = vec[0]
        for i in xrange(len(vec)):
            vec[i] -= tmp
            if vec[i] < 0:
                vec[i] += 26

        return ''.join([chr(x + ord('a')) for x in vec])
        
