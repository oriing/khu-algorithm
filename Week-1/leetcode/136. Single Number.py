class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        before = set()
        for val in nums:
            if val in before:
                before.remove(val)
            else:
                before.add(val)
        return list(before)[0]