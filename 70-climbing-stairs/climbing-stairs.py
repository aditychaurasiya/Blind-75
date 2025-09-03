import math

class Solution:
    def comb(self, n, r):
        return math.comb(n, r)
    
    def climbStairs(self, n: int) -> int:
        total = 0
        for k in range(n // 2 + 1):
            total += self.comb(n - k, k)
        return total
