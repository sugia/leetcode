class Solution:
    #given a list of integers
    #return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        res = []
        self.cal(num, [], res)
        return res
    def cal(self, num, cur, res):
        if len(num) == 0:
            res.append(cur)
            return
        can = set()
        for i in range(len(num)):
            if num[i] in can:
                continue
            can.add(num[i])
            self.cal(num[:i] + num[i+1:], cur + [num[i]], res)
