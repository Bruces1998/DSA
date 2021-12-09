#include <stdio.h>

int memo[4][4] = {0};
int cost[4][4] = {{0, 10, 75, 94}, {-1, 0, 35, 50}, {-1, -1, 0, 80},
                {-1, -1, -1, 0}};



int minCost(int s, int d){
  	if (s==d || s==d-1){
		return cost[s][d];}


	if (memo[s][d] ==0){




	int min = cost[s][d];

	for (int i=s+1; i < d; i++){
		int temp = minCost(s, i) + minCost(i, d);
		if (temp < min){
			min = temp;}
	}

	memo[s][d] = min;
	}

	return memo[s][d];
}


int main(void){
	int ans = minCost(0,3);
	printf("%d", ans);
}

