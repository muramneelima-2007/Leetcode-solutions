class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> m1;
        for(int i=0;i<s.size();i++){
            m1[s[i]]=m1[s[i]]+1;
        }
        map<char,int> m2;
        for(int i=0;i<t.size();i++){
            m2[t[i]]=m2[t[i]]+1;
        }
        return m1==m2;
    }
};