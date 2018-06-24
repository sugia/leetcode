'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []



'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        if not num:
            return res

        for i in xrange(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.find(num[i:], int(num[:i]), target, num[:i], res, int(num[:i]))
        
        return res
    
    def find(self, num, tmpsum, target, tmp, res, last):
        if not num:
            if tmpsum == target:
                res.append(tmp)
            return
        
        for i in xrange(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.find(num[i:], tmpsum + int(num[:i]), target, tmp + '+' + num[:i], res, int(num[:i]))
                self.find(num[i:], tmpsum - int(num[:i]), target, tmp + '-' + num[:i], res, -int(num[:i]))
                self.find(num[i:], tmpsum - last + last * int(num[:i]), target, tmp + '*' + num[:i], res, last * int(num[:i]))
                
