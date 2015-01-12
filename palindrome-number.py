class Solution:
    #given an integer
    #return a bool
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        step = 1
        y = x
        while y > 0:
            step *= 10
            y //= 10
        step //= 10
        while x > 0:
            if x // step != x % 10:
                return False
            x = (x % step) // 10
            step //= 100
        return True
