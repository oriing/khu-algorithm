class Solution:
    def per(self, nums, used, i, n, ans, lst):
        if i == n:
            ans.append(lst.copy())
        else:
            for t in range(n):
                if used & (2**t): continue
                lst.append(nums[t])
                self.per(nums, used|(2**t), i+1, n, ans, lst)
                del lst[-1]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        lst = []
        self.per(nums, 0, 0, len(nums), ans, lst)

        return ans