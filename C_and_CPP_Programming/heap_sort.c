#include <stdio.h>

void adjust(int *a, int i, int n);

void main(void){
	int n, a[20], t;
	printf("Enter array size:");
	scanf("%d", &n);

	for(int i = 1; i<= n; i++)
	{
		printf("\nEnter element number %d:",i);
		scanf("%d", &a[i]);
	}

	for (int i = n/2; i >= 1; i--)
	{
		adjust(a, i, n);
	}

	for(int i=n; i >=2; i--)
	{
		t = a[1];
		a[1] = a[i];
		a[i] = t;
		adjust(a, 1, i-1);
	}

	printf("The sorted array is:\n");

	for (int i = 1; i <=n; i++)
	{
		printf("%d\n", a[i]);
	}



}

void adjust(int *a, int i, int n){
	int x, j;
	x = a[i];
	j = i*2;

	while(j <= n){
		if (j < n && a[j] < a[j+1]){
			j++;
		}

		if (x > a[j]){
			break;
		}

		a[j/2] = a[j];
		j = j*2;
	}

	a[j/2] = x;
}
