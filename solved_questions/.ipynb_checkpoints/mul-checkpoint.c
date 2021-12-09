#include <stdio.h>


int mul(int n, int m);

int main(void)
{
  int a = mul(0, 0);
  printf("%d", a);
}







int mul(int n, int m)
{
  if (m==0)
  {
    return 1;
  }
  if (m == 1)
  {
    return n;
  }

  return n + mul(n, m-1);
}
