class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mva = max(prices)

        for val in prices:
            if val < mva:
                mva = val
            ans = max(ans, val - mva)
            
        return ans