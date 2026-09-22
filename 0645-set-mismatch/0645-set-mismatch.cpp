class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n=nums.size();
        vector <int> arr(n+1); 
        for(int i=0;i<n;i++){
            arr[nums[i]]+=1;
        }
        int dup;
        int lost;
        for(int i=1;i<arr.size();i++){
            if(arr[i]==0){
                lost=i;
            }
            else if(arr[i]==2){
                dup=i;
            }
        }
        vector <int> res={dup,lost};
        return res;
    }
};