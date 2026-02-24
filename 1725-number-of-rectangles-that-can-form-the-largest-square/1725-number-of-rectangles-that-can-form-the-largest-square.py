class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxSide=0
        c=0
        for rect in rectangles:
            s=min(rect)
            if(s>maxSide):
                maxSide=s 
        for i in rectangles:
            if(min(i)==maxSide):
                c=c+1
        return c


