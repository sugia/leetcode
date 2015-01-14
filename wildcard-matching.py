class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        i = 0
        j = 0
        save = 0
        star = -1
        while i < len(s):
            if j < len(p) and p[j] == '?':
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                j += 1
                save = i
            elif j < len(p) and s[i] == p[j]:
                i += 1
                j += 1
            elif star != -1:
                j = star + 1
                save += 1
                i = save
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j >= len(p)
