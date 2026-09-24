class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li=[]
        m=max(candies)
        for i in candies:
            if(i+extraCandies>=m):
                li+=[True]
            else:
                li+=[False]
        return li
