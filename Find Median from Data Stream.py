'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2


'''

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.b = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.a, -num)
        top = -heapq.heappop(self.a)
        heapq.heappush(self.b, top)
        
        if len(self.a) < len(self.b):
            top = heapq.heappop(self.b)
            heapq.heappush(self.a, -top)
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.a) == len(self.b):
            return (-self.a[0] + self.b[0]) * 0.5
        else:
            return -self.a[0] * 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
