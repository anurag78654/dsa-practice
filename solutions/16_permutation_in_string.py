# Pattern: Sliding Window (fixed-size + sort)
# Intuition: window size = len(s1); sort window and compare to sorted s1

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            w = ''.join(sorted(s2[l:r+1]))
            if w == s1:
                return True
            l += 1
            r += 1
        return False