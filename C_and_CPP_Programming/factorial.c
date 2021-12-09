#include <stdio.h>
int factorial(int n);

int main(void){
    int n;
    printf("Enter Input: ");
    scanf("%d",&n);
    printf("Value is %d", factorial(n));

    return 0;


}

int factorial(int n){
    if (n==1){
        return 1;
    }

    return n*factorial(n - 1);
}