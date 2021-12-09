#include <bits/stdc++.h>
using namespace std;

bool findWinner(int x, int y, int n){
    int dp[n+1];
    dp[0] = false;
    dp[1] = true;

    for(int i = 2; i <= n; i++){

        if(i-1>=0 && !dp[i-1]){
            dp[i] = true;
        }
        else if (i - x >= 0 && !dp[i-x]){
            dp[i] = true;
        }
        else if (i - y >= 0 && !dp[i-y]){
            dp[i] = true;
        }
        else{
            dp[i] = false;
        }
    }

    return dp[n];
}

int main()
{
    int x, y, n;
    cin >>n;
    cin>>x;
    cin>>y;
    if (findWinner(x, y, n))
        cout << 'A';
    else
        cout << 'B';
 
    return 0;
}