#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int maxProfit(int k, vector<int> prices){
    int len = prices.size();
    if (len < 2) return 0;
    if(k > len/2){
        int ans = 0;
        for(int i = 1; i < len; i++){
            ans+= max(prices[i] - prices[i-1], 0);
        }

        return ans;
    }

    int hold[k+1];
    int release[k+1];

    for(int i = 0; i <= k; i++){
        hold[i] = INT_MIN;
        release[i] = 0;
    }

    int curr = 0;
    for(int i = 0; i < len; i++){
        curr = prices[i];
        for(int j = k; j > 0; j--){
            release[j] = max(release[j], hold[j]+curr);
            hold[j] = max(hold[j], release[j-1] - curr);
        }   
    }
    return release[k];
    
}

int main(){
    vector <int> arr = {3, 2, 6, 5, 0, 3};
    int k = 2;
    cout << maxProfit(k, arr);
    return 0;
}