class Solution {
public:
    bool product(int n,int t){
            int temp=n;
            int p=1;
            int last;
            while(n!=0){
                last=n%10;
                p=p*last;
                n=n/10;
            }
            if(p%t==0){
                return true;
            }
            return false;
        }
    int smallestNumber(int n, int t) {
        while(1){
            if(product(n,t)){
                return n;
            }
            n++;
        }
    }
};