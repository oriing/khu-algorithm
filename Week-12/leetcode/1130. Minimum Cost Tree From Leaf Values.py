class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        d   = [float('inf')]
        ans = 0
        for i in arr:
            while d[-1] <= i:
                val  = d.pop()
                ans += val * min(d[-1], i)
            d.append(i)

        while len(d) > 2:
            ans += d.pop() * d[-1]
        
        return ans