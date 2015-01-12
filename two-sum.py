class Solution:
    #given a list of integers and an integer
    #return a tuple (index1, index2), they are not zero-based
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            map[num[i]] = i
        for i in range(len(num)):
            tmp = target - num[i]
            if tmp in map:
                if i < map[tmp]:
                    return (i+1, map[tmp]+1)
                elif i > map[tmp]:
                    return (map[tmp]+1, i+1)
        return (0, 0)
