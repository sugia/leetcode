'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.vec = []
        self.size = size
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.vec and len(self.vec) >= self.size:
            tmp = self.vec.pop(0)
            self.total -= tmp
        self.vec.append(val)
        self.total += val
        return 1.0 * self.total / len(self.vec)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
