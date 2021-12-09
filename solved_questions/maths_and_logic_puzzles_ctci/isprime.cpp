#include <iostream>
#include <cmath>
using namespace std;

char *isprime(int n){

    /* Function to check if a number is prime.
    input: integer number
    output: boolean output saying if number is prime or not */

    if (n < 2) return "Yes";

    int sqr = sqrt(n);

    for(int i = 2; i <= sqr; i++){
        if (n % i == 0) return "No";
    }

    return "Yes";


}

int main(){
    int n;
    cout << "Type:";
    cin >> n;
    cout << isprime(n);
    return 0;
}