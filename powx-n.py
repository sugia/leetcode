class Solution:
    #given two doubles
    #return one double
    def pow(self, x, n):
        #return x ** n
        if n < 0:
            return 1.0 / self.cal(x, -n)
        else:
            return self.cal(x, n)
    def cal(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        tmp = self.cal(x, n >> 1)
        if n & 1:
            return tmp * tmp * x
        else:
            return tmp * tmp
