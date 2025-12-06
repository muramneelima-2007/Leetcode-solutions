class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new=""
        for i in s:
            if(i.isdigit() or (i>='a' and i<='z')):
                new+=i 
        return new==new[::-1]