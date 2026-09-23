class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=set(nums)
        if(len(n)<3):
            return max(nums)
        else:
            li=list(n)
            m1=-100000000000
            m2=-100000000000
            m3=-100000000000
            for i in li:
                if(i>m1 and i>m2 and i>m3):
                    m3=m2
                    m2=m1
                    m1=i 
                elif(i<m1 and i>m2 and i>m3):
                    m3=m2 
                    m2=i 
                elif(i<m1 and i<m2 and i>m3):
                    m3=i 
            return m3
            
