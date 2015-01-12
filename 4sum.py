class Solution:
    #given a list of integers and an integer
    #return a list of lists of integers
    def fourSum(self, num, target):
        num.sort()
        map = {}
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                tmp = num[i] + num[j]
                if tmp not in map:
                    map[tmp] = [[i, j]]
                else:
                    map[tmp].append([i, j])
        res = []
        can = set()
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                tmp = target - num[i] - num[j]
                if tmp in map:
                    for x in map[tmp]:
                        if j < x[0]:
                            cur = [num[i], num[j], num[x[0]], num[x[1]]]
                            if tuple(cur) not in can:
                                can.add(tuple(cur))
                                res.append(cur)
        return res
