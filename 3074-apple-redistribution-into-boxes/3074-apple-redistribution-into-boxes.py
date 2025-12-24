class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity=sorted(capacity,reverse=True)
        total=sum(apple)
        count=0
        for i in capacity:
            total=total-i
            count=count+1
            if(total<=0):
                return count

