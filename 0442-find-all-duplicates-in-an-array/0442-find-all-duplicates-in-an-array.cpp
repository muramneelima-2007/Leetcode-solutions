class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n=nums.size();
        vector <int> res;
        vector <int> v(n+1);
        for(int i=0;i<n;i++){
            v[nums[i]]=v[nums[i]]+1; 
        }
        for (int i=0;i<n+1;i++){
            if(v[i]==2){
                res.push_back(i);
            }
        }
        return res;
    }
};