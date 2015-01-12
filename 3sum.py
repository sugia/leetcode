class Solution:
    #given a list of integers
    #return a list of lists of integers
    def threeSum(self, num):
        num.sort()
        res = []
        i = 0
        while i < len(num) - 2:
            j = i + 1
            k = len(num) - 1
            while j < k:
                tmp = num[i] + num[j] + num[k]
                if tmp < 0:
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                elif tmp > 0:
                    k -= 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                else:
                    res.append([num[i], num[j], num[k]])
                    j += 1
                    k -= 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
            i += 1
            while i < len(num) - 2 and num[i] == num[i-1]:
                i += 1
        return res
