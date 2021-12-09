#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Job
{
    /* data */
    int start, finish, profit;
};

bool jobComparator(Job s1, Job s2){

    return (s1.finish < s2.finish);
}

int latestNonConflict(vector<Job> arr, int i){

    for(int j = i; j >=0; j++){
        if(arr[j].finish <= arr[i-1].start){
            return j;
        }
    }

    return -1;
}

int findMaxProfitRec(vector<Job> arr, int n){
    if (n == 1){
        return arr[n-1].profit;
    }

    int incluProf = arr[n-1].profit;
    int i = latestNonConflict(arr, n);

    if(i != -1){
        incluProf += findMaxProfitRec(arr, i+1);
    }

    int excluProf = findMaxProfitRec(arr, n-1);

    return max(incluProf, excluProf);
}

int findMaxProfit(vector<Job> arr, int n)
{
    // Sort jobs according to finish time
    sort(arr.begin(), arr.end(), jobComparator);
 
    return findMaxProfitRec(arr, n);
}
 
// Driver program
int main()
{
    vector<Job> arr = {{3, 10, 20}, {1, 2, 50}, {6, 19, 100}, {2, 100, 200}};
    int n = 4;
    cout << "The optimal profit is " << findMaxProfit(arr, n);
    return 0;
}

