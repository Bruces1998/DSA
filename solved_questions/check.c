#include <stdio.h>
#include <string.h>

void print(char * C)
{
	// int i = 0;
	while(*C != '\0')
	{
		printf("%c", *C);
		C++;
	}

	printf("\n");
}
void main(void){
	char C[20] = "Aniket";
	print(C);
	print(C);

}
