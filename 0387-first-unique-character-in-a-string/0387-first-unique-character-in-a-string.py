class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        char=""
        for i in s:
            d[i]=0 
        for i in s:
            d[i]=d[i]+1 
        for i,j in d.items():
            if(j==1):
                char=i 
                break
        for i in range(len(s)):
            if(s[i]==char):
                return i 
        return -1                
