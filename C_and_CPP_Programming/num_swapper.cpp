//Program to swap two numbers in place
#include <iostream>
using namespace std;

void swap(int &x, int &y){
    x = x + y;
    y = x - y;
    x = x - y;
}

int main() 
{ 
    int x, y; 
    printf("Enter Value of x "); 
    scanf("%d", &x); 
    printf("\nEnter Value of y "); 
    scanf("%d", &y); 
    swap(x, y); 
    printf("\nAfter Swapping: x = %d, y = %d\n", x, y); 
    return 0; 
} 