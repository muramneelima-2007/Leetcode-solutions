class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li=[]
        for n in range(left,right+1):
            c=0 
            m=n
            while(m!=0):
                t=m%10 
                if(t==0):
                    break
                if(n%t==0):
                    c=c+1
                else:
                    break
                m=m//10 
            if(c==len(str(n))):
                li.append(n)
        return li

