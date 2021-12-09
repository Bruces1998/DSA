#include <iostream>
using namespace std;
# define NO_OF_CHARS 256


void badHeu (string str, int badchar[NO_OF_CHARS]){
    int size = str.size();
    for (int i = 0; i < NO_OF_CHARS; i++){
        badchar[i] = -1;
    }

    for (int i = 0; i < size; i++){
        badchar[(int) str[i]] = i;
    } 

}

void search(string txt, string pat){
    int m = pat.size();
    int n = txt.size();

    int badchar[NO_OF_CHARS];

    badHeu(pat, badchar);
    int s = 0;

    while( s <= n - m){
        int j = m - 1;

        while( j >= 0 && pat[j] == txt[s+j] ){
            j--;
        }

        if (j < 0){
            cout << "pattern found at shift = " << s << endl;
            s += (s + m < n) ? m - badchar[txt[s + m]] : 1;
        }

        else{

            s += max(1, j - badchar[txt[s + j]]);
        }

    }
}


int main()
{
    string a = "hello";
    string pat = "olle";
    search(a, pat);
    return 0;

}