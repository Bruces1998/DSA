#include <stdio.h>

int minCost(int s, int d, int cost[][]){
	if (s==d || s==d-1)
		return cost[s][d];

	int minC = cost[s][d];
	for (int i= s+1; i < d; i++){
		int temp = minCost(s, i) + minCost(i, d);
	
		if (temp < minC)
			minC = temp;


	}

	return minC;

}

void main(void){
	
	int cost[4][4] = {{ 0, 10, 75, 94}, {-1, 0, 35, 50},{-1, -1, 0, 80}, {-1, -1, -1, 0}};

	printf("%d",minCost(0, 3, cost);

			}
