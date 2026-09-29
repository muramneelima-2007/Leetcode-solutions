class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=0 
        for i in s:
            d[i]=d[i]+1
        res=sorted(d.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for item in res:
            ans+=item[0]*item[1]
        return ans