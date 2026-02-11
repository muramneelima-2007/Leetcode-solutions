class Solution:
    def freqAlphabets(self, s: str) -> str:
        n=len(s)
        res=""
        k=n-1
        while k>=0:
            if(s[k]=='#'):
                w=int(s[k-2]+s[k-1])
                res=res+chr(96+w)
                k=k-3
            else:
                m=int(s[k])+96
                res=res+chr(m)
                k=k-1
        return res[::-1]
        
                