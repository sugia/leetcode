class Solution:
    #given two strings
    #return a list of integer
    def findSubstring(self, s, p):
        n = len(p)
        if n == 0:
            return []
        m = len(p[0])
        if m == 0:
            return []
        map = {}
        for x in p:
            if x not in map:
                map[x] = 1
            else:
                map[x] += 1
        res = []
        for i in range(len(s) + 1 - n * m):
            tmp = {}
            flag = True
            for j in range(n):
                word = s[i+j*m:i+j*m+m]
                if word not in map:
                    flag = False
                    break
                if word not in tmp:
                    tmp[word] = 1
                else:
                    tmp[word] += 1
                if tmp[word] > map[word]:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res
