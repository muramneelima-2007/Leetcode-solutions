class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        l=len(grid[0])
        for li in grid:
            for j in range(l):
                if(li[j]<0):
                    c=c+1
        return c
