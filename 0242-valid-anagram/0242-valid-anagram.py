class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p=Counter(s)
        c=Counter(t)
        if(sorted(p.keys()) != sorted(c.keys())):
            return False 
        for key,value in c.items():
            if(c[key]==p[key]):
                continue
            else:
                return False
        return True 

        # p=[]
        # c=[]
        # for i in s:
        #     p=p+[i]
        # for i in t:
        #     c=c+[i]
        # p.sort()
        # c.sort()
        # if(p==c):
        #     return True
        # return False


    
