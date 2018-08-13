'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

 

Note:

    0 <= A.length <= 200
    0 <= B.length <= 200
    A and B both contain only spaces and lowercase letters.


'''

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        a_dic = self.getDic(A)
        b_dic = self.getDic(B)
        
        res = []
        for k, v in a_dic.iteritems():
            if v == 1:
                if k not in b_dic:
                    res.append(k)
                    
        for k, v in b_dic.iteritems():
            if v == 1:
                if k not in a_dic:
                    res.append(k)
                    
        return res
    
    def getDic(self, s):
        vec = s.split()
        dic = {}
        for token in vec:
            if token in dic:
                dic[token] += 1
            else:
                dic[token] = 1
                
        return dic
