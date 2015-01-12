class Solution:
    #given an integer
    #return a list of strings
    def generateParenthesis(self, n):
        res = []
        self.cal(n, n, '', res)
        return res
    def cal(self, i, j, cur, res):
        if i == 0 and j == 0:
            res.append(cur)
            return
        if i > 0:
            self.cal(i-1, j, cur + '(', res)
        if j > i:
            self.cal(i, j-1, cur + ')', res)
