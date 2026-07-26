class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int n1=nums[0]*nums[1]*nums[n-1];
        int n2=nums[n-1]*nums[n-2]*nums[n-3];
        if(n1>n2){
            return n1;
        }
        return n2;
    }
};