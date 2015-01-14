class Solution:
    #given two strings
    #return one string
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i]) * int(num2[j])
        for i in range(len(res)-1):
            res[i+1] += res[i] // 10
            res[i] %= 10
        if res[-1] == 0:
            res.pop()
        return ''.join(str(x) for x in res[::-1])
