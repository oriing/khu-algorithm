class Solution:
    # Boyer-Moore vote algorithm
    def majorityElement(self, nums: List[int]) -> int:
        t = 0

        for val in nums:
            if t == 0:
                major = val
            if major != val:
                t -= 1
            if major == val:
                t += 1
        return major