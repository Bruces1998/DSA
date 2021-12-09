#include <iostream>
#include <vector>
using namespace std;
int min(int a, int b){
    return a < b ? a:b;
}
int car_assembly(vector<vector<int>> a, vector<vector<int>> t, int *e, int *x){

    int n = a.size();
    int T1[n], T2[n], i;

    T1[0] = e[0] + a[0][0];
    T2[0] = e[1] + a[1][0];

    for(i = 1; i < n; i++){

        T1[i] = min(T1[i-1]+a[0][i], T2[i-1] + t[1][i] + a[0][i] );
        T2[i] = min(T2[i-1]+a[1][i], T1[i-1] + t[0][i] + a[1][i] );
    }

    return min(T1[n-1] + x[0], T2[n-1] + x[1]);
}

int main()
{
    vector<vector<int>> a = {{4, 5, 3, 2},
                            {2, 10, 1, 4}};
    vector<vector<int>> t = {{0, 7, 4, 5},
                            {0, 9, 2, 8}};
    int e[] = {10, 12}, x[] = {18, 7};
 
    cout << car_assembly(a, t, e, x);
 
    return 0;
}