class Solution {
public:
    int countValidPrefixes(string s) {
        int c0=0;
        int c1=0;
        int count=0;
        for(int i=0;i<s.length();i++){
            if(s[i]=='1'){
                c1++;
            }
            else{
                c0++;
            }
            if(abs(c0-c1)<=1){
                    count++;
            }
        }
        return count;
    }
};