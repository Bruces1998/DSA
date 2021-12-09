#include <iostream>

using namespace std;

int main(){
    //Section 1
    // int var1;
    // int var2[10];

    // cout << "Address of var1: ";
    // cout << &var1 << endl;

    // cout << "Address of var2: ";
    // cout << &var2 << endl;

    // cout << "Address of var1: ";
    // cout << var1 << endl;

    // cout << "Address of var2: ";
    // cout << *(var2+1) << endl;

    // return 0;


    //Section 2

    // int var = 20;
    // int *ip;

    // ip = &var;

    // cout << "Value";
    // cout << var << endl;

    // cout << "Address";
    // cout << ip << endl;

    // cout << "Value:";
    // cout << *ip << endl;

    // return 0;

    char *arr = (char *)calloc(5, sizeof(char));
    for (int i = 0; i < 5; i++){
        arr[i] = 'a';
    }

    for (int i = 0; i < 5; i++){
        cout << (int)arr[i] << endl;
    }

    free(arr);
}