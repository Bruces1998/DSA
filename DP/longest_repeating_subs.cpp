#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int lcs_repeated(int x, int y, string s1, string s2)
    {
        // your code here
        int mapp[x+1][y+1];
        for(int i = 0; i <=x; i++) mapp[i][0] = 0;
        for(int j = 0; j <=y; j++) mapp[0][j] = 0;
        
        for(int i = 1; i <= x; i++)
        for(int j = 1; j <= y; j++){
            if (i!=j && s1[i-1] == s2[j-1]){
            mapp[i][j] = 1 + mapp[i-1][j-1];
            }
            
            else{
                mapp[i][j] = max(mapp[i-1][j], mapp[i][j-1]);
            }
        
        
        }
        return mapp[x][y];
        
    }
int main(){
    string s1 = "aab";
    cout << lcs_repeated(3, 3, s1, s1);
    return 0;

}
