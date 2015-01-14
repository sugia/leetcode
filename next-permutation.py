class Solution:
    #given a list of integers
    #return a list of integers
    def nextPermutation(self, num):
        if len(num) == 0:
            return []
        idx = -1
        for i in range(len(num)-1)[::-1]:
            if num[i] < num[i+1]:
                idx = i
                break
        if idx == -1:
            return sorted(num)
        idy = len(num) - 1
        for i in range(len(num))[::-1]:
            if num[i] > num[idx]:
                idy = i
                break
        tmp = num[idx]
        num[idx] = num[idy]
        num[idy] = tmp
        return num[:idx+1] + num[idx+1:][::-1]
