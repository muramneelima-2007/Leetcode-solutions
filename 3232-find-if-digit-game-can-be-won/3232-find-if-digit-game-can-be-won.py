class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s=0
        d=0
        for i in nums:
            if(i<10):
                s=s+i 
            else:
                d=d+i
        if(s!=d):
            return True
        return False        