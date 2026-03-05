class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        res=""
        for i in s:
            res=res+i 
            for k in strs[1:]:
                if(k.startswith(res)):
                    continue 
                else:
                    return res[:-1]
        return res

                    

            