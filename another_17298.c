#include <stdio.h>
int main(int argc, char** argv)
{
	int input_num;
	scanf("%d",&input_num);
	int result_list[input_num];
	int stack_list[input_num];
	int input_list[input_num];
	int top = 0;
	stack_list[top] = 0;
	for (int i = 0; i<input_num; i++)
	{
		int elem;
		scanf("%d",&elem);
		for (int j = top; j > 0; j--)
		{
			if (input_list[stack_list[j]] >elem-1) break;
			result_list[stack_list[j]] = elem;
			top --;
		}
		result_list[i] = -1;
		top++;
		stack_list[top] = i;
		input_list[i] = elem;
	}
	for (int i = 0; i<input_num;i++)
		{
			printf("%d ",result_list[i]);
		}
	return 0;	
}