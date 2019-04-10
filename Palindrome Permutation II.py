'''
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []

'''

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        
        
        odd_count = 0
        odd_c = None
        for c in dic:
            if dic[c] & 1:
                odd_count += 1
                dic[c] -= 1
                odd_c = c
                
        if odd_count > 1:
            return []
        
        tmp = ''
        if odd_count == 1:
            tmp = odd_c
        
        res = set()
        self.find(dic, len(s), tmp, res)
        return list(res)
    
    def find(self, dic, length, tmp, res):
        if len(tmp) == length:
            res.add(tmp)
            return
        
        for c in dic:
            if dic[c] == 0:
                continue
            
            dic[c] -= 2
            self.find(dic, length, c + tmp + c, res)
            
            dic[c] += 2
            
        
        
