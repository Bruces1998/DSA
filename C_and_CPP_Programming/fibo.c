#include <stdio.h>
int fibo(int n);

int main(void){
    int n;
    printf("Enter Input: ");
    scanf("%d",&n);
    printf("Value is %d", fibo(n));

    return 0;


}

int fibo(int n){
    if (n == 0 || n == 1){
        return n;
    }

    return fibo(n - 1) + fibo(n - 2);
}