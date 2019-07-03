#include <stdio.h>
int main(int argc, char* argv[])
{
	int input_num;
	scanf("%d",&input_num);
	int list_for_result[input_num];
	int list_index = 0, result = 0;
	while(input_num--)
	{
		int list_element;
		scanf("%d",&list_element);
		if (list_element)
		{
			list_for_result[list_index] = list_element;
			list_index ++;
		} 
		else list_index--;

	}
	while (list_index--)
	{
		result += list_for_result[list_index];
	}
	printf("%d",result);
}