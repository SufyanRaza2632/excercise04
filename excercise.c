#include <stdio.h>

int main()
{
	int input,number,sum=0;                                // 3 integers declared
	scanf("%d",&input);				       // user input is taken

	printf("%d \n",input);
	number = input;

	while ( number != 0)				       //loop until the user input is reduced to 0
	{
		sum = sum+ (number % 10 );
		number = number / 10;
	}
	
	int difference = input - sum ;                        //takes difference of input number and its digit sum

	printf("The difference between the input and its digit sum is %d \n",difference);
	return 0;
}
