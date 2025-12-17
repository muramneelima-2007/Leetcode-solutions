class Solution {
    public int maxProfit(int[] prices) {
        int maxi=0;
        int n=prices.length;
        int[] arr=new int[n];
        int val=Integer.MIN_VALUE;
        for(int i=n-1;i>=0;i--)
        {
            val=Math.max(val,prices[i]);
            arr[i]=val;
        }
        for(int i=0;i<n-1;i++)
        {
            maxi=Math.max(maxi,(arr[i+1]-prices[i]));
        }
        return maxi;
    }
}