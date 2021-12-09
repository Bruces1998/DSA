#include <iostream>

using namespace std;

int catalanNum(int n){

    if(n<=1){
        return 1;
    }

    unsigned long int res = 0;
    for(int i = 0; i < n; i++){
        res += catalanNum(i) * catalanNum(n - i - 1);
    }

    return res;
}


int catalanDP(int n){
    long int catal[n+1];

    catal[0] = catal[1] = 1;

    for(int i = 2; i <= n; i++){
        catal[i] = 0;
        for(int j = 0; j < i; j++){
            catal[i] += catal[j] * catal[i-j-1];
        }
    }

    return catal[n];
}

int main(){
    for(int i = 0; i < 10; i++){
        cout << catalanNum(i) << " ";
        
    }
    for(int i = 0; i < 10; i++){
    cout << catalanDP(i) << " ";
    }
    return 0;
}