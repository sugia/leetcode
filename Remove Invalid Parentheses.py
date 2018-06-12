'''

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        vec = set([s])
        while len(vec):
            next_vec = set()
            for item in vec:
                if self.valid(item) and item not in next_vec:
                    next_vec.add(item)
                    
            if next_vec:
                return list(next_vec)
            
            for item in vec:
                for i in xrange(len(item)):
                    tmp = item[:i] + item[i+1:]
                    if tmp not in next_vec:
                        next_vec.add(tmp)
                    
            vec = next_vec
                    
        return []
    
    def valid(self, item):
        count = 0
        for c in item:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        
        if count == 0:
            return True
        return False
