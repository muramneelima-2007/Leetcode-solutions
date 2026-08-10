class Solution {
public:
    int hammingWeight(int n) {
        int count=0;
        int t;
        while(n!=0){
            t=n%2;
            if(t==1){
                count++;
            }
            n=n/2;
        }
        return count;
    }
};