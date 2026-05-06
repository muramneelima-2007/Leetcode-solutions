class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for w in words:
            wt=0
            for k in w:
                n=ord(k)-97
                wt+=weights[n]
            c=wt%26
            num=(26-c-1)+97
            res=res+chr(num)
        return res

