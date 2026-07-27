class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n=nums.size();
        int max=nums[0];
        int min=nums[n-1];
        vector <int> vmax;
        vmax.push_back(max);
        vector <int> vmin;
        vmin.push_back(min);
        for(int i=1;i<n;i++){
            if(nums[i]>max){
                max=nums[i];
            }
            vmax.push_back(max); 

            if(nums[n-i-1]<min){
                min=nums[n-i-1];
            }  
            vmin.push_back(min); 
        }
        reverse(vmin.begin(),vmin.end());
        for(int i=0;i<n;i++){
            if(vmax[i]-vmin[i]<=k){
                return i;
            }
        }
        return -1;
    }
};