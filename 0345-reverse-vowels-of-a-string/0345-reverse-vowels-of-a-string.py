class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['A','E','I','O','U','a','e','i','o','u']
        li=[]
        for i in s:
            if(i in vowels):
                li.append(i)
        li=li[::-1]
        res=""
        k=0
        for i in range(len(s)):
            if(s[i] in vowels):
                res=res+li[k]
                k=k+1
            else:
                res=res+s[i]
        return res