class Solution:
    #given a string
    #return an integer
    def romanToInt(self, s):
        key = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = 0
        for i in range(len(key)):
            while len(key[i]) <= len(s) and key[i] == s[:len(key[i])]:
                res += val[i]
                s = s[len(key[i]):]
        return res
