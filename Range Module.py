'''
A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
Note:

A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.
'''

class RangeModule:

    def __init__(self):
        self.pairs = []

    def addRange(self, left: int, right: int) -> None:
        new_pairs = [[left, right]]
        for p in self.pairs:
            if p[1] < new_pairs[-1][0]:
                tmp = new_pairs.pop()
                new_pairs.append(p)
                new_pairs.append(tmp)
            elif new_pairs[-1][1] < p[0]:
                new_pairs.append(p)
            else:
                new_pairs[-1][0] = min(new_pairs[-1][0], p[0])
                new_pairs[-1][1] = max(new_pairs[-1][1], p[1])
        self.pairs = new_pairs
        
    def queryRange(self, left: int, right: int) -> bool:
        l = 0
        r = len(self.pairs) - 1
        while l <= r:
            m = (l + r) // 2
            if right <= self.pairs[m][0]:
                r = m - 1
            elif self.pairs[m][1] <= left:
                l = m + 1
            else:
                return self.pairs[m][0] <= left and right <= self.pairs[m][1]
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_pairs = []
        for p in self.pairs:
            if right <= p[0] or p[1] <= left:
                new_pairs.append(p)
            else:
                if p[0] < left:
                    new_pairs.append([p[0], left])
                if right < p[1]:
                    new_pairs.append([right, p[1]])
        
        self.pairs = new_pairs

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
