class Solution {
    public int searchInsert(int[] nums, int target) {
        int index=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==target)
            {
                index=i;
            }
            else
            {
                for(int k=0;k<nums.length-1;k++)
        {
         if(nums[k]<target && nums[k+1]>target)
            {
                index=k+1;
            }
            if(nums[k+1]<target)
            {
                index=k+2;
            }
           
            
        }
        if(nums.length==1)
        {
            if(nums[0]<target)
        {
            index=1;
        }
        }
       

            }
            
        }
         
        return index;
    }
}