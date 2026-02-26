class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        w=""
        length=len(s)
        for i in range(length):
            w=w+s[i]
            if(len(w)==k):
                res.append(w)
                w=""
            if(i==length-1):
                n=len(w)
                if(n!=0):
                    word=w+fill*(k-n)
                    res.append(word)
        return res
