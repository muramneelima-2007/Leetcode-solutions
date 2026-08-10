class Solution {
public:
    int hammingDistance(int x, int y) {
        int n=x^y; 
        int t;
        int count=0;
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