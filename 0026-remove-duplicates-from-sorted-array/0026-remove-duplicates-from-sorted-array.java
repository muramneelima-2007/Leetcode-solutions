class Solution {
    public int removeDuplicates(int[] nums) {
    HashSet<Integer> hs=new HashSet<>();
    for(int n:nums)
    {
        hs.add(n);
    }
    int i=0;
    for(int c:hs)
    {
        nums[i++]=c;
    }
    for(int j=i;j<nums.length;j++)
    {
        nums[j]=1000;
    }
    Arrays.sort(nums);
    return hs.size();
    }
}