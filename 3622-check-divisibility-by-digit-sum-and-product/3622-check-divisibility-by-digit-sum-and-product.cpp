class Solution {
public:
    bool checkDivisibility(int n) {
        int num=n;
        int psum=1;
        int dsum=0;
        while(n!=0){
            int temp=n%10;
            psum*=temp;
            dsum+=temp;
            n=n/10;
        }
        if(num%(psum+dsum)==0){
            return true;
        }
        return false;
    }
};