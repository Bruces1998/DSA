#include <iostream>
#include <climits>
#include <map>

using namespace std;

map<int, int> memo;
int egg_drop(int floors, int eggs){

    if(floors == 0 || floors == 1 || eggs == 1){
        return floors;
    }
    if (memo.find(floors) == memo.end()){
        int min = INT_MAX;

        for(int p = 1; p <=floors; p++ ){

            int temp = max(egg_drop(p-1, eggs - 1), egg_drop(floors - p, eggs));

            if(temp < min) min = temp;

        memo[floors] = min+1;
        }
    }
    

    return memo[floors];
}


int main(){
    cout << egg_drop(100, 2) << '\n';
}