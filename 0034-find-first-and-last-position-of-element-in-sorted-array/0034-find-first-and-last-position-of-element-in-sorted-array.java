class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n=nums.length;
        int left=0;
        int right=n-1;
        boolean fleft=false;
        boolean fright=false;
        int start=-1;
        int end=-1;
        while(left<=right)
        {
            if(nums[left]==target && !fleft)
            {
                fleft=true;
            }
            else if(nums[left]!=target)
            {
                left++;
            }
            if(nums[right]==target && !fright)
            {
                fright=true;
            }
            else if(nums[right]!=target)
            {
                right--;
            }
            if(fleft && fright)
            {
                start=left;
                end=right;
                break;
            }
        }
        int[] arr=new int[2];
        arr[0]=start;
        arr[1]=end;
        return arr;
    }
}