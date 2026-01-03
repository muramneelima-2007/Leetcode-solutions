class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        s1.extend(s2)
        d={}
        for i in s1:
            d[i]=0 
        for i in s1:
            d[i]=d[i]+1 
        res=[]
        for key,val in d.items():
            if(val==1):
                res.append(key)
        return res