#include <stdio.h>
int *sorted_merge(int *A, int *B);
void main(void){
  int a[10],b[5];
  int *p;
  printf("\nEnter element in array A:\n");

	for(int i = 0; i<= 4; i++)
	{
		scanf("%d", &a[i]);
	}

  printf("\nEnter element in array B:\n");
  for(int i = 0; i<= 4; i++)
	{
		scanf("%d", &b[i]);
	}
  p = sorted_merge(a,b);

  printf("\nElements are:\n");
  for(int i = 0; i<= 9; i++)
	{
		printf("%d\n", p[i]);
	}


}

int *sorted_merge(int *A, int *B)
{
  int i,j,k;
  int m = 10; //sizeof A / sizeof *A;
  int n = 5; //sizeof B / sizeof *B;
  printf("%d\n",m );
  printf("%d\n",n );
  i = m - n -1;
  j = n - 1;
  k = m - 1;
  while(i > -1 && j > -1)
  {
    while( A[i] > B[j])
    {
      A[k] = A[i];
      k--;
      i--;
    }

    while(A[i] <= B[j])
    {
      A[k] = B[j];
      k--;
      j--;
    }

  }

  if (i <= -1)
  {
    while(j != -1)
    {
      A[k] = B[j];
      j--;
      k--;
    }
  }

  if (j <= -1)
  {
    while(i != -1)
    {
      A[k] = A[i];
      i--;
      k--;
    }
  }

  return A;
}
