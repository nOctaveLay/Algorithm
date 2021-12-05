#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void print_error();
void detect_error();

//error case들 : )(, ))(, ()), ((), ([]], [()), []], [[],][,][]

int main(int argc, char *argv)
{
	char in_string[30];
	int list_string[30];
	int stack_count = 0;
	int result = 0;
	int list_i = 0;
	scanf("%s",&in_string);
	int len_string = strlen(in_string);
	for (int i = 0; i<len_string;i++)
	{
		if (in_string[i] == '(') list_string[list_i] = -1;
		else if (in_string[i] == '[') list_string[list_i] = -2;
		else if (in_string[i] == ')')
		{
			list_i --;
			if (list_i < 0) print_error();
			else if (list_string[list_i] == -1) list_string[list_i] = 2;
			else if (list_string[list_i] > 0) 
			{
				list_i --;
				if (list_string[list_i] != -1) print_error();
				else list_string[list_i] = list_string[list_i+1] * 2;
			}
			else print_error();
		}
		else
		{
			list_i --;
			if (list_i < 0) print_error();
			else if (list_string[list_i] == -2) list_string[list_i] = 3;
			else if (list_string[list_i] > 0) 
			{
				list_i --;
				if (list_string[list_i] != -2) print_error();
				else list_string[list_i] = list_string[list_i+1] * 3;
			}

			else print_error();
		}
		if (list_i > 1 && list_string[list_i] >0 && list_string[list_i-1] > 0)
		{
			list_i --;
			list_string[list_i] += list_string[list_i +1];
		
		}
		list_i ++;
	}
	for (list_i; list_i > 0 ; list_i--)
	{
		list_string[list_i-1] > 0 ? result = result + list_string[list_i-1] : print_error();
	}
	printf("%d\n",result);
}

void print_error()
{
	printf("0\n");
	exit(0);
}
