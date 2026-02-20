class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n=len(words)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                w=words[j]
                if(words[i]==w[::-1]):
                    c+=1
        return c
