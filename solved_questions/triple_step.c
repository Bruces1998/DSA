#include <stdio.h>

int climbStairs( int n);
int step(int n, int memo[]);

int main(void)
{
	int n;
	scanf("%i",&n);
	printf("%i\n", climbStairs(n));
	// getchar();
}
int step(int n, int memo[])
{
	if (n < 0)
	{
		return 0;
	}

	else if (n == 0)
	{
		return 1;

	}

	else if (memo[n]>-1)
	{
		return memo[n];
	}

	else
	{
		memo[n] = step(n-1, memo) + step(n - 2, memo) + step(n-3, memo);
		return memo[n];
	}
}

int climbStairs(int n)
{
	int arr[n+1];
	for (int i = 0; i <= n; i++)
	{
		arr[i] = -1;
	}

	return step(n, arr);

}
