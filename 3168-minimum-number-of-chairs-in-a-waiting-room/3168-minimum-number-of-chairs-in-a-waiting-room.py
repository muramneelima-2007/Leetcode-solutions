class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        l=0
        for i in s:
            if(i=="E"):
                if(l>0):
                    l=l-1
                else:
                    c=c+1
            else:
                l=l+1
        return c
