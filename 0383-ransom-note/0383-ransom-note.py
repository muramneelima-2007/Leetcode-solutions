class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=list(ransomNote)
        m=list(magazine)
        r.sort()
        m.sort()
        n=len(m)
        k1=0
        k2=0
        while n!=0:
            if(r[k1]==m[k2]):
                k1=k1+1 
                if(k1==len(r)):
                    return True
            k2=k2+1
            n=n-1

        return False

