class Solution:
    def canJump(self, nums: List[int]) -> bool:
        now: int = nums[0]
        if now == 0 and len(nums) > 1: return False
        for i in range(1, len(nums)-1):
            now -= 1
            now  = max(now, nums[i])
            if now == 0:
                return False
        return True
