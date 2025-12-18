class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        k=0
        n=numRows
        while k!=n:
            if(k==0):
                res.append([1])
            elif(k==1):
                res.append([1,1])
            else:
                prev=res[k-1]
                new=[prev[0]]
                l=len(prev)
                for i in range(l-1):
                    new=new+[prev[i]+prev[i+1]]
                new=new+[prev[-1]]
                res.append(new)
                new=[]
            k=k+1 
        return res   