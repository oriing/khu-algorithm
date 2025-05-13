class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        val = 1
        for i in range(1, n+m-1): val  *= i
        for i in range(1, n):     val //= i
        for i in range(1, m):     val //= i
        return val