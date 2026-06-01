class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m=len(mat)
        fn=mat
        while(k!=0):
            matrix=[]
            for i in range(m):
                if(i%2==0):
                    li=mat[i]
                    li=li[1:]+[li[0]]
                else:
                    li=mat[i]
                    li=[li[-1]]+li[:-1]
                matrix.append(li)
            mat=matrix
            k=k-1
        if(mat==fn):
            return True
        return False
