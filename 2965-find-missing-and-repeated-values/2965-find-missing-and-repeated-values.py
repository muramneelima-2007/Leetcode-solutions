class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d={}
        res=[]
        n=len(grid[0])
        for i in grid:
            for j in i:
                d[j]=0
        for i in grid:
            for j in i:
                d[j]=d[j]+1 
        li=list(d.keys())
        for i,j in d.items():
            if(j>1):
                res.append(i)
                break
        li.sort()
        k=0
        found=False
        for i in range(1,len(li)+1):
            if(li[k]!=i):
                res.append(i)
                found=True
                break
            k=k+1
        if(found==False):
            res.append(n*n)
        return res
        

        




      