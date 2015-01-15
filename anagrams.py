class Solution:
    #given a list of strings
    #return a list of strings
    def anagrams(self, strs):
        map = {}
        for x in strs:
            word = ''.join(sorted(list(x)))
            if word not in map:
                map[word] = [x]
            else:
                map[word].append(x)
        res = []
        for x in map:
            if len(map[x]) > 1:
                res += map[x]
        return res
