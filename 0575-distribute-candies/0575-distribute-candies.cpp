class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        sort(candyType.begin(),candyType.end());
        int n=candyType.size();
        int h=n/2;
        int count=1;
        for(int i=1;i<n;i++){
            if(candyType[i]!=candyType[i-1]){
                count++;
            }
        }
        if(h>count){
            return count;
        }
        return h;
    }
};