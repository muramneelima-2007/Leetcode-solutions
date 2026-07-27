class Solution {
public:
    int findGCD(vector<int>& nums) {
        int max=nums[0];
        int min=nums[0];
        for(auto i=nums.begin();i<nums.end();i++){
            if((*i)>max){
                max=*i;
            }
            if((*i)<min){
                min=*i;
            }
        }
        while(max!=0 && min!=0){
            if(max>min){
                max=max%min;
            }
            else{
                min=min%max;
            }
        }
        if(max==0){
            return min;
        }
        return max;
    }
};