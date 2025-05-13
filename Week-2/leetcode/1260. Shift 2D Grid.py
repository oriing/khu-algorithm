class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans    = [[0]*len(grid[0]) for i in range(len(grid))]
        ans_1D = [0]*len(grid[0])*len(grid)
        NM     = len(grid[0])*len(grid)

        ival   = 0
        for i in grid:
            for j in i:
                ans_1D[(ival+k)%NM] = j
                ival               += 1
        
        ival   = 0
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                ans[i][j] = ans_1D[ival]
                ival     += 1
        
        return ans
