#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int contigousSum(vector<int> arr){
    int sum = 0;
    int max = 0;
    int n = arr.size();
    for (int i = 0; i < n; i++){
        sum += arr[i];
        if (max < sum){
            max = sum;
        }

        else if (sum < 0){
            sum = 0;
        }
    }
        

    return max;
}

int main(){
    vector<int> a = {2, -8, 3, -2, 4, -10};
    int b = contigousSum(a);
    cout << b << " \n";
}