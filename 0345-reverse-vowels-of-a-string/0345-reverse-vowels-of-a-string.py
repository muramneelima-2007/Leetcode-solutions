class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['A','E','I','O','U','a','e','i','o','u']
        # li=[]
        # for i in s:
        #     if(i in vowels):
        #         li.append(i)
        # li=li[::-1]
        # res=""
        # k=0
        # for i in range(len(s)):
        #     if(s[i] in vowels):
        #         res=res+li[k]
        #         k=k+1
        #     else:
        #         res=res+s[i]
        # return res
        left=0
        s=list(s)
        right=len(s)-1
        res=""
        while left<right:
            if(s[left] in vowels):
                if(s[right] in vowels):
                    temp=s[left]
                    s[left]=s[right]
                    s[right]=temp
                else:
                    right-=1
            else:
                left+=1 
        return s
    