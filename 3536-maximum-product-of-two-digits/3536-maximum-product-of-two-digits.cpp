class Solution {
public:
    int maxProduct(int n) {
        /*vector <int> v;
        int t;
        while(n!=0){
            t=n%10;
            v.push_back(t);
            n=n/10;
        }
        sort(v.begin(),v.end(),greater<int>());
        return v[0]*v[1];*/
        int max1=0;
        int max2=0;
        int t;
        while(n!=0){
            t=n%10;
            if(t>max1){
                max2=max1;
                max1=t;
            }
            else if(t>max2){
                max2=t;
            }
            n=n/10;
        }
        return max1*max2;

    }
};