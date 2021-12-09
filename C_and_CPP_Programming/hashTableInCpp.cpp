#include <iostream>
#include <unordered_map>

using namespace std;

int main(){

    unordered_map<string, int> umap;

    umap["name"] = 1;
    umap["age"] = 2;
    umap["time"] = 3;

    for (auto x: umap){
        cout << x.first << " " << x.second << endl;
    }
}