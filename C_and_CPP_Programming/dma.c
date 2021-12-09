#include <stdio.h>
#include <stdlib.h>

void main(void)
{
  int m;
  int *a;
  int *b = malloc(sizeof(int));
  a = &m;
  a = b;
  m = 10;
  *b = 10;
  *b = m + 2;
  printf("%i\n",*b );
  free(b);
  *a = 11;

  printf("%i\n %i",*a, m);

}
