

//Eh trying to write more efficient code, first try was terrible
class Solution {
public:
    int numDecodings(string s) {
        vector<int> tab(s.length()+1, 0);

        tab[0] = 1;
        if(s[0]-'0' == 0){
            tab[1] = 0;
            return 0;//Leading zeroes case
        } else {
            tab[1] = 1;
        }
        cout<< s[1];
      
        for(int i = 1; i < s.length(); ++i){
            if((s[i]-'0') + 10*(s[i-1]-'0') <= 26 && (s[i]-'0') + 10*(s[i-1]-'0') >= 10){

                tab[i+1] += tab[i-1];
            }//Check for twodigit numbers
            if(s[i]-'0'<= 9 && s[i] -'0' > 0) {
                tab[i+1] += tab[i];
            }// Check for 1 digit numbers
        }
        return tab[s.length()];
        

    }
};
