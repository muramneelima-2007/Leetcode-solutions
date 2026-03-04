class Solution {
    public boolean isPalindrome(int x) {
        int t=x,sum=0;
        while(x>0)
        {
            int y=x%10;
            sum=(sum*10)+y;
            x=x/10;
        }
        if(sum==t)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}