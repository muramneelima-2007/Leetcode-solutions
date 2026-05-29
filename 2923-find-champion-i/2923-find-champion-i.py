class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ind=0
        for i in range(n):
            c=0
            for j in range(n):
                if(grid[i][j]==1):
                    c=c+1 
            if(c>=n-1):
                return i
