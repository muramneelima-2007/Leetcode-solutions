class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n=nums.length;
        int tsub=1<<n;
        List<List<Integer>> list = new ArrayList<>();
        for(int i=0;i<tsub;i++)
        {
            ArrayList<Integer> al=new ArrayList<>();
            for(int j=0;j<n;j++)
            {
                if((i & (1<<j))!=0)
                {
                   al.add(nums[j]);
                }
            }
            list.add(al);
        }
        return list;
    }
}