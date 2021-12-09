#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int minJumps( int arr[],int n){

    if (n == 1){
        return 0;
    }

    vector<int> dp(INT_MAX, n);

    for(int i = n - 2; i>=0; i--){
        if (arr[i] >= n-1-i){
            dp[i] = 1;
        }

        else{
            for(int j = 1; j<= arr[i]+1; j++){
                if (i+j < n && dp[i+j]!= -1){
                    dp[i] = min(dp[i], 1 + dp[i+j]);
                }
            }
        }
    }

    if (dp[0] == INT_MAX){
        return -1;
    }

    return dp[0];
}


int main(){
    int arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9};
    cout << minJumps(arr, 11);

}