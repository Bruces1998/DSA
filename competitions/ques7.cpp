#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int get_expansion(){

    int n;
    std::string s;
    std::cin >> n >> s;
    std::vector<std::vector<int> > vec;

    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++){
            // cout << i << j << "\n";
            std::vector<int> v1;
            v1.push_back(i);
            v1.push_back(j);
            vec.push_back(v1);


        }

    }

    int m = vec.size();
    if (m == 1){
        return 1;
    }

    std::vector<int> dp(m, 1);

    for(int i = 0; i < m-1; i++)
    for(int j = i+1; j < m; j++){
        if(s.substr(vec[j][0], vec[j][1]) >= s.substr(vec[i][0], vec[i][1])){
            dp[j] = std::max(dp[j], 1+dp[i]);
        }
    }

    return *max_element(dp.begin(), dp.end());



    

    
}


int main() {
	std::ios::sync_with_stdio(0); std::cin.tie(0);
	
	int t; std::cin >> t;
	while (t--) {
		std::cout << get_expansion()<<"\n";
	}
}