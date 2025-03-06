class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            current = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    current += 1
            
            ans.append(current)
            # 배열 크기(500) > 숫자 범위(101) 이므로 dict로 시간 단축 가능하나
            # N값이 작아 유의미하지는 X
        
        return ans