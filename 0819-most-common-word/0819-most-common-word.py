class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        s=paragraph.lower()
        st=""
        for i in s:
            if((i>='a' and i<='z') or i==" "):
                st=st+i 
            else:
                st=st+" "
        li=list(st.split()) 
        d={}
        for i in li:
            d[i]=0 
        for i in li:
            d[i]=d[i]+1 
        maxi=0 
        for i,j in d.items():
            if((i not in banned) and j>maxi):
                maxi=j 
        for i,j in d.items():
            if(i not in banned and j==maxi):
                return i 

