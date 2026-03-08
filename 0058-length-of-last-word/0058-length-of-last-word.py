class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        li=s.split()
        res=li[-1]
        return len(res)
        