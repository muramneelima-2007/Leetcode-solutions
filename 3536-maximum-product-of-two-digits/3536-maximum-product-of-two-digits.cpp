class Solution {
public:
    int maxProduct(int n) {
        vector <int> v;
        int t;
        while(n!=0){
            t=n%10;
            v.push_back(t);
            n=n/10;
        }
        sort(v.begin(),v.end(),greater<int>());
        return v[0]*v[1];
    }
};