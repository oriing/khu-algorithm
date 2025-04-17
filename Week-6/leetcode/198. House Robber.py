class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        
        dp = [0]*len(nums)
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2]+nums[0]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        
        return max(dp[-1], dp[-2], dp[-3])