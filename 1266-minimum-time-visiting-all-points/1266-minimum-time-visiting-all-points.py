class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        total=0
        for i in range(n-1):
            p1=points[i]
            p2=points[i+1]
            dx=abs(p2[0]-p1[0])
            dy=abs(p2[1]-p1[1])
            total+=max(dx,dy)
        return total