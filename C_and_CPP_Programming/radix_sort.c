#include <stdio.h>

void radix_sort(int *a, int n);


void main(void){
	int n, a[20];
	printf("Enter array size:");
	scanf("%d", &n);

	for(int i = 0; i<= n -1; i++)
	{
		printf("\nEnter element number %d:",i+1);
		scanf("%d", &a[i]);
	}

  radix_sort(a, n);

  printf("The sorted array is:\n");

	for (int i = 0; i <=n - 1; i++)
	{
		printf("%d\n", a[i]);
	}
}
void radix_sort(int *a, int n){
  int i, j, e = 1, c[10], bucket[20][10], k, z;
  int digit;
  for (int i = 1; i <= 3; i++){


    for (int j = 0; j <= 9; j++){
      c[j] = -1;
    }

    for (int j = 0; j <= n-1; j++){
      digit = (a[j]/e)%10;
      c[digit]++;
      bucket[c[digit]][digit] = a[j];
    }

    z = 0;

    for(int j = 0; j <= 9; j++){
      if (c[j] != -1){
        for (k = 0; k <= c[j]; k++){
          a[z] = bucket[k][j];
          z++;
        }
      }
    }
    e = e*10;
  }
}
