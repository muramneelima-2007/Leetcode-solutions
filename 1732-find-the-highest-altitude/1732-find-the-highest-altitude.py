class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        li=[0]
        c=0
        for i in gain:
            c=c+i
            li.append(c)
        return max(li)