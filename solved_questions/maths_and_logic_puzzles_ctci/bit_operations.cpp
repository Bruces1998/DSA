#include <iostream>
#include <cmath>
using namespace std;

int clear_bit(int n, int i){
    int mask = ~(1 << i);
    n = n & mask;
    return mask;

}

int main(){
    int n;
    cout << "Type:";
    cin >> n;
    cout << clear_bit(n, 3);
    return 0;
}