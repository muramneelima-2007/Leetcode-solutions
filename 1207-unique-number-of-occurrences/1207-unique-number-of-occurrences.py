class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            c=arr.count(i)
            d[i]=c 
        s=d.values()
        l1=len(set(s))
        l2=len(s)
        if(l1==l2):
            return True 
        return False
        