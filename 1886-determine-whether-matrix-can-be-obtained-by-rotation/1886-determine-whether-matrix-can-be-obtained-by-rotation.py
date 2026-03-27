class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            new=[]
            c=len(mat)
            r=len(mat)
            for i in range(c):
                row=[]
                for j in range(r):
                    row=[mat[j][i]]+row
                new.append(row)
            return new 
        r=4
        if(mat==target):
            return True
        while(r!=0):
            new=rotate(mat)
            mat=new
            if(new==target):
                return True
            else:
                new=rotate(mat)
            r=r-1
        return False

