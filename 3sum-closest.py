class Solution:
    #given a list of integers and an integer
    #return an integer
    def threeSumClosest(self, num, target):
        assert len(num) >= 3
        num.sort()
        cdiff = abs(num[0] + num[1] + num[2] - target)
        res = num[0] + num[1] + num[2]
        i = 0
        while i < len(num) - 2:
            j = i + 1
            k = len(num) - 1
            while j < k:
                tmp = num[i] + num[j] + num[k]
                diff = tmp - target
                if abs(diff) < cdiff:
                    cdiff = abs(diff)
                    res = tmp
                if diff < 0:
                    j += 1
                elif diff > 0:
                    k -= 1
                else:
                    return res
            i += 1
        return res
