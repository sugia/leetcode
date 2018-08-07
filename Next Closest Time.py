'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.


'''

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        res = []
        digits = [time[0], time[1], time[3], time[4]]
        
        self.build(digits, res)
        
        ans = None
        for t in res:
            if not ans or self.dis(t, time) < self.dis(ans, time):
                ans = t
                
        return ans
        
    def build(self, digits, res):
        for a in digits:
            for b in digits:
                for c in digits:
                    for d in digits:
                        tmp = a + b + ':' + c + d
                        if self.valid(tmp):
                            res.append(tmp)
    
    def valid(self, tmp):
        if int(tmp[:2]) < 24 and int(tmp[3:]) < 60:
            return True
        return False
        
    def dis(self, nex, cur):
        nex_min = int(nex[:2]) * 60 + int(nex[3:])
        cur_min = int(cur[:2]) * 60 + int(cur[3:])
        
        res = nex_min - cur_min
        if res <= 0:
            res += 24 * 60
        
        return res
