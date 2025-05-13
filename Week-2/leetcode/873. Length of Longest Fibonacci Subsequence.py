class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        N   = len(arr)
        dp  = [[2]*N for i in range(N)]
        ans = 0
        dic = {arr[i]:i for i in range(len(arr))}
        
        # for k in range(N):
        #     for j in range(k): // j, k 반복문 순서 상관 없음
        for j in range(N-1):
            for k in range(j+1, N):
                iv = arr[k]-arr[j]
                if iv in dic and dic[iv] < j:
                    i        = dic[iv]
                    dp[j][k] = max(dp[j][k], dp[i][j]+1)
                    ans      = max(dp[j][k], ans)
        
        return ans