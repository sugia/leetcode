'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        key = ''
        for c in s:
            key += c
            if len(key) > 10:
                key = key[1:]
            
            if len(key) == 10:
                if key not in dic:
                    dic[key] = 0
                dic[key] += 1
        
        res = []
        for key in dic:
            if dic[key] > 1:
                res.append(key)
        
        return res
