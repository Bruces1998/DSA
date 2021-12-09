#include <iostream>
#include <string>

using namespace std;

int edit_distance(string a, string b, int m, int n){

    int editM[m+1][n+1];

    for(int i = 0; i <= m; i++){
        editM[i][0] = i;
    }

    for(int j = 0; j <= n; j++){
        editM[0][j] = j;
    }

    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){

            if (a[i-1] == b[j-1]){
                editM[i][j] = editM[i-1][j-1];
            }

            else{
                editM[i][j] = min(editM[i-1][j-1], min(editM[i-1][j], editM[i][j-1])) + 1;
            }
        }
    }

    return editM[m][n];
}

int main(){
    string a;
    string b;
    cin >> a;
    cin >> b;
    int m = a.size();
    int n = b.size();

    cout << edit_distance(a, b, m, n) << "\n";
}