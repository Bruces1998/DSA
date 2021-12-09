#include <iostream>
#include <vector>

using namespace std;

long long int countPS(string str){
    if (str.size() <= 0){
        return 1;
    }
    if (str.size() == 1){
        return 0;
    }

    int n = str.size();
    if (str[0] == str[n-1]){
        cout<<"here";
        return countPS(str.substr(1, n-1))+ countPS(str.substr(0, n-1))+ countPS(str.substr(1, n-2));
    }

    else{
        cout<<"here" << "\n";
        return countPS(str.substr(1, n-1))+ countPS(str.substr(0, n-1));
    }

}

int main(){
    string s;
    cin >> s;
    cout << countPS(s);
    return 0;
}