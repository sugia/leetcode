class Solution:
    #given a string
    #return a list of strings
    def letterCombinations(self, digits):
        map = {0:'', 1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        '''
        que = ['']
        for i in range(len(digits)):
            nex = []
            for x in que:
                for y in map[int(digits[i])]:
                    nex.append(x + y)
            que = nex
        return que
        '''
        res = []
        self.cal(map, digits, 0, '', res)
        return res
    def cal(self, map, digits, i, cur, res):
            if i == len(digits):
                res.append(cur)
                return
            for x in map[int(digits[i])]:
                self.cal(map, digits, i+1, cur + x, res)
