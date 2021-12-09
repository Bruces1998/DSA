#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int max_sum(vector<int> arr){
    
    int max_sum_ending_here = 0;
    int max_sum_till_now = 0;

    for(int i = 0; i < arr.size(); i++){
        max_sum_ending_here += arr[i];

        if (max_sum_ending_here < 0){
            max_sum_ending_here = 0;
        }

        if (max_sum_till_now < max_sum_ending_here){
            max_sum_till_now = max_sum_ending_here;
        }
    }

    return max_sum_till_now;
}

int main(){

    vector<int> a = {-2, -3, 4, -1, -2, 1, 5, -3};
    cout << max_sum(a)<< "\n";

}
