class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total=0
        time=0
        n=len(timeSeries)
        for i in range(n-1):
            if(timeSeries[i+1]>=timeSeries[i]+duration):
                total+=duration
            else:
                total+=(timeSeries[i+1]-timeSeries[i])
        return total+duration

            

