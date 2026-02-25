class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOnes(b):
            c=0
            for i in b:
                if(i=='1'):
                    c=c+1
            return c
        dic={}
        for i in range(len(arr)):
            bn=bin(arr[i])[2:]
            count=countOnes(bn)
            dic[i]=count
        d={}
        for v in dic.values():
            d[v]=list()
        for k,v in dic.items():
            d[v]=d[v]+[arr[k]]
        for k,v in d.items():
            d[k].sort()
        ones=list(d.keys())
        ones.sort()
        res=[]
        for i in ones:
            res.extend(d[i])
        return res
            