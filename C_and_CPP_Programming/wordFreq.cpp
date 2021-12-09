#include <iostream>
#include <unordered_map>
#include <bits/stdc++.h> 

using namespace std;



void printFreq(string str){

    unordered_map<string, int> hashTable;

    string word;
    stringstream s(str);

    while (s >> word){
        hashTable[word]++;
    }

    for (auto i: hashTable){
        cout << i.first << " " << i.second << "\n";
    }

}

int main(){
    string str = "geeks for geeks geeks quiz "
                 "practice qa for"; 
    printFreq(str); 
    return 0; 

}