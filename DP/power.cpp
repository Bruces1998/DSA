#include <iostream>

using namespace  std;

int power(int x,int n){
    if(n == 0){
        return 1;

    }

    if(x == 1){
        return x;
    }

    return x*power(x, n-1);


}

int main(){
    int x, n;
    printf("Enter Value of x "); 
    scanf("%d", &x);

    printf("Enter Value of n "); 
    scanf("%d", &n);

    cout << power(x, n);

}