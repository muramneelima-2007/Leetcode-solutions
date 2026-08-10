class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int ind=0;
        int temp;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0){
                temp=nums[i];
                nums[i]=nums[ind];
                nums[ind]=temp;
                ind++;
            }
        }
    }
};