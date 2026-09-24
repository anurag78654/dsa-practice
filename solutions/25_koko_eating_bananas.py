# Pattern: Binary Search (on answer)
# Intuition: binary search eating speed; hours needed via ceil(p/k)

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
        return result