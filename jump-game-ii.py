class Solution:
    #given a list of integers
    #return an integer
    def jump(self, num):
        step = 0
        i = 0
        tmp = 0
        while i < len(num):
            nex = tmp
            while i < len(num) and i <= tmp:
                nex = max(nex, i + num[i])
                i += 1
            tmp = nex
            step += 1
        return step - 1
