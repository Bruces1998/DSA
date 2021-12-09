#include <iostream>
#include <unordered_map>
#include <bits/stdc++.h>

using namespace std;

int sum(vector<int> arr){
    int n = sizeof(arr)/sizeof(arr[0]);
    int sum = 0;
    for (int i = 0; i < n; i++){
        sum += arr[i];
    }

    return sum;
}

vector<int> swapSum(vector<int> a,vector<int> b){
    int sum1 = accumulate(a.begin(), a.end(), 0);
    int sum2 = accumulate(b.begin(), b.end(), 0);
    vector<int> ans = {-1, -1};
    int target = (sum1 - sum2) / 2;
    cout << target << "\n";
    unordered_map<int , int> hash_table;

    for (auto x: b){
        hash_table[target + x] = x;
    }

    for (auto y: a){
        if (hash_table.find(y) == hash_table.end()){
            continue;
        }
        else{

            ans[0] = y;
            ans[1] = hash_table[y];
        }
    }

    return ans;

}

int main(){
    vector<int> a = {4, 1, 2, 1, 1, 2};
    vector<int> b = {3, 6, 3, 3};
    vector<int> p = swapSum(a, b);

    cout << p[0] << " " << p[1] << "\n";
    return 0; 

}

