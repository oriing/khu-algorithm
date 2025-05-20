class Solution:
    def subxor(self, nums, sval, i, n):
        if i == n: return sval
        return self.subxor(nums, sval, i+1, n) + self.subxor(nums, sval^nums[i], i+1, n)
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.subxor(nums, 0, 0, len(nums))