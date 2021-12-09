#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<int> subSort(vector<int> a){
    int n = a.size();
    vector<int> ans;
    int i = 0;
    int j = n -1;

    while(i != n-1 && a[i] <= a[i+1]){
        i++;
    }

    while(j != 0 && a[j] >= a[j-1]){
        j--;
    }

    sort(a.begin() + i + 1, a.begin() + j - 1);
    
    while (a[i] > a[i+1])
    {
        i--;
        sort(a.begin() + i + 1, a.begin() + j);
    }

    while (a[j] < a[j - 1]){
        j++;
        sort(a.begin() + i, a.begin() + j - 1);
    }

    ans = {i, j};

    return ans;


}

int main(){
    vector<int> a = {1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16,18, 19 };
    vector<int> b = subSort(a);
    cout << b[0] << " " << b[1] << "\n";
    return 0;
}