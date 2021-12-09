#include <iostream>
#include <string>

using namespace std;

bool recursive_sol(string a, string b, string c){
    if (a[0]=='\0' && b[0]=='\0' && c[0]=='\0'){
        return true;
    }

    if(c[0] == '\0'){
        return false;
    }

    if(a[0] == '\0' && b[0] == '\0'){
        return false;
    }

    bool first = false;
    bool sec = false;

    if(a[0] == c[0]){
        first = recursive_sol(a.substr(1, a.size() - 1), b, c.substr(1, c.size() - 1));
    }


    if(b[0] == c[0]){
        sec = recursive_sol(a, b.substr(1, b.size() - 1), c.substr(1, c.size()-1));
    }


    return (first || sec);
}


bool dp_sol(string a, string b, string c){
    int m = a.size();
    int n = b.size();

    if(c.size() != m+n){
        return false;
    }

    bool mat[m+1][n+1];

    mat[0][0] = true;

    for(int i = 1; i<=m; i++){
        if(a[i-1] != c[i-1]){
            mat[i][0] = false;
        }

        else{
            mat[i][0] = mat[i-1][0];
        }
    }

    for(int i = 1; i<=n; i++){
        if(b[i-1] != c[i-1]){
            mat[0][i] = false;
        }

        else{
            mat[0][i] = mat[0][i-1];
        }

    }


    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){

            if(a[i-1] == c[i+j-1] && b[j-1]!=c[i+j-1]){
                mat[i][j] = mat[i-1][j];
            }

            else if(a[i-1] != c[i+j-1] && b[j-1]==c[i+j-1]){
                mat[i][j] = mat[i][j-1];
            }

            else if(a[i-1] == c[i+j-1] && b[j-1]==c[i+j-1]){
                mat[i][j] = mat[i][j-1] || mat[i-1][j];
            }


            else{
                mat[i][j] = false;
            }




        }
    

    
    }

    return mat[m][n];
}

int main(){
    string a;
    string b;
    string c;
    cin >> a;
    cin >> b;
    cin >> c;

    cout << recursive_sol(a, b, c) << "\n";
    cout << dp_sol(a, b, c) << "\n";
}