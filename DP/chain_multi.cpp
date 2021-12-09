#include <iostream>
#include<climits>
using namespace std;

int calculate(int *arr,int start, int end){

    int ans = 1;

    for(int i = start; i<=end; i++){
        ans *= arr[i];
    }

    return ans;
}

int chain_multi(int *arr, int start, int end){
    if (start == end){
        return 0;
    }

    int mini = INT_MAX;
    int count;

    for(int k = start; k < end; k++){

        count = chain_multi(arr, start, k) + chain_multi(arr, k+1, end) + arr[start-1]*arr[k]*arr[end];

        mini = min(count, mini);
    }

    return mini;

}

int main(){
    int arr[5] = {40, 20, 30, 10, 30};
    cout << chain_multi(arr, 1, 4);
    return 0;
}