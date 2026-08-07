class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size();
        int n1=nums2.size();
        vector <int> res; 
        for(int i=0;i<n;i++){
            bool isFound=false;
            int next=-1;
            for(int j=0;j<n1;j++){
                if(nums1[i]==nums2[j]){
                    isFound=true;
                }
                if(nums2[j]>nums1[i] && isFound){
                    next=nums2[j];
                    break;
                }
            }
            res.push_back(next);
        }
        return res;
    }
};