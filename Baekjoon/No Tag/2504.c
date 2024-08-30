#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void print_error();
int detect_error(int list_string[30],int list_i,char backet);

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
		if (in_string[i] == '(') list_string[list_i] = -2;
		else if (in_string[i] == '[') list_string[list_i] = -3;
		else if (in_string[i] == ')') list_i = detect_error(list_string,list_i,')');
		else list_i = detect_error(list_string,list_i,']');

		if (list_i > 1 && list_string[list_i] >0 && list_string[list_i-1] > 0)
		{
			list_i --;
			list_string[list_i] += list_string[list_i +1];
		}

		list_i ++;
	}
	for (list_i; list_i > 0 ; list_i--)
	{
		list_string[list_i-1] > 0 ? result += list_string[list_i-1] : print_error();
	}
	printf("%d\n",result);
}

void print_error()
{
	printf("0\n");
	exit(0);
}

int detect_error(int list_string[30],int list_i,char backet)
{
	int what;
	if (backet == ')') what = 2;
	else what = 3;

	list_i --;
	if (list_i < 0) print_error();
	else if (list_string[list_i] == -what) list_string[list_i] = what;
	else if (list_string[list_i] > 0) 
	{
		list_i --;
		if (list_string[list_i] != -what) print_error();
		else list_string[list_i] = list_string[list_i+1] * what;
	}
	else print_error();
	what = 0;
	return list_i;
}
