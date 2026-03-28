class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n=len(s)
        c=0
        v=['a','e','i','o','u']
        if(s[-1] not in v):
            return s
        for i in range(n):
            if(s[n-i-1] in v):
                c=c+1
            else:
                break 
        return s[:n-c]
            