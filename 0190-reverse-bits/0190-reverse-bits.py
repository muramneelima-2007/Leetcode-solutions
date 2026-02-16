class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)[2:].zfill(32)
        res=0
        for i in range(32):
            d=int(b[i])
            mul=2**i
            res=res+(d*mul)
        return res

