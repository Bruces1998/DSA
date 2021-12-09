#include <stdio.h>
#include <time.h>
int fibo(int i);

int main(void)
{
        clock_t tic = clock();
        int n;
        scanf("%i",&n);
        printf("%d", fibo(n));
        getchar();
        clock_t toc = clock();

        printf("Elapsed: %f seconds \n", (double)(toc - tic) / CLOCKS_PER_SEC);
        return 0;
}

int fibo(int i)
{
    if (i==0)
    {
	return 0;
    }

    int a = 0;
    int b = 1;
    for (int i = 2; i < 2; i++)
    {
	int c = a + b;
	a = b;
	b = c;
    }

    return a + b;
}

