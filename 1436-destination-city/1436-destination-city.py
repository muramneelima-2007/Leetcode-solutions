class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=[]
        end=[]
        for i,j in paths:
            start.append(i)
            end.append(j)
        for i in range(len(end)):
            if(end[i] not in start):
                return end[i]

            
            
    