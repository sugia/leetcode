class Solution:
    #given a list of integers and an integer
    #return a list of lists of integers
    def combinationSum2(self, num, target):
        res = []
        self.cal(sorted(num), target, 0, [], res)
        return res
    def cal(self, num, target, i, cur, res):
        if target == 0:
            res.append(cur)
            return
        can = set()
        for j in range(i, len(num)):
            if num[j] > target:
                return
            if num[j] in can:
                continue
            can.add(num[j])
            self.cal(num, target - num[j], j+1, cur + [num[j]], res)
