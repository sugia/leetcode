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
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        
        if not self.small:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
            
        while self.small and self.large and -self.small[0] > self.large[0]:
            if len(self.small) > len(self.large):
                top = -heapq.heappop(self.small)
                heapq.heappush(self.large, top)
            else:
                top = heapq.heappop(self.large)
                heapq.heappush(self.small, -top)
        
        while len(self.small) - len(self.large) > 1:
            top = -heapq.heappop(self.small)
            heapq.heappush(self.large, top)
            
        while len(self.large) - len(self.small) > 1:
            top = heapq.heappop(self.large)
            heapq.heappush(self.small, -top)
            
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -self.small[0] * 1.0
        else:
            return self.large[0] * 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
