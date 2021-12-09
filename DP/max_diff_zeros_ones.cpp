#include <iostream>
#include <climits>
#include <vector>
using namespace std;

int get_max(vector<int> arr){
    int maxx = INT_MIN;
    int n = arr.size();

    for(int i = 0; i < n; i++){
        maxx = max(maxx, arr[i]);
    }

    return maxx;
}

int maxSubstring(string S){
    int n = S.size();
    vector<int> dp(n, 0);

    if(S[0] == '1'){
        dp[0] = -1;
    }

    else{
        dp[0] = 1;
    }

    for(int i = 1; i < n; i++){
        if(S[i] == '1'){
            dp[i] = max(-1, dp[i-1]-1);
        }

        else{
            dp[i] = max(1, dp[i-1]+1);
        }
    }

    return get_max(dp);
}

int main(){
    string s= "11000010001";
    cout << maxSubstring(s);
    return 0;
}