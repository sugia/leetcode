class Solution:
    #given a list of integers
    #return an integer
    def firstMissingPositive(self, num):
        if len(num) == 0:
            return 1
        num.sort()
        i = 0
        while i < len(num) and num[i] < 1:
            i += 1
        if i >= len(num):
            return 1
        if num[i] > 1:
            return 1
        while i + 1 < len(num) and num[i] + 1 >= num[i+1]:
            i += 1
        return num[i] + 1
