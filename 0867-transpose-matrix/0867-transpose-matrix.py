class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        res=[]
        k=0
        while(c!=0):
            row=[]
            for i in range(r):
                row.append(matrix[i][k])
            k=k+1
            res.append(row)
            c=c-1
        return res
