class Solution:
    #given an integer
    #return a string
    def intToRoman(self, num):
        key = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        t = ''
        for i in range(len(key)):
            while num >= val[i]:
                t += key[i]
                num -= val[i]
        return t
