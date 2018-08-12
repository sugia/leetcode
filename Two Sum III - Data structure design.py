'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false


'''

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_count = {}
        self.found = set([])

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.num_count:
            self.num_count[number] += 1
        else:
            self.num_count[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value in self.found:
            return True
        for k, v in self.num_count.iteritems():
            if value - k in self.num_count:
                if value - k == k:
                    if v > 1:
                        self.found.add(value)
                        return True
                else:
                    self.found.add(value)
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
