/* 실행되지 않음 */
#include <stdio.h>
int main(int argc, char** argv)
{
	int input_num;
	scanf("%d",&input_num);
	int nge_list[input_num+1];

	for (int i = 0; i<input_num; i++)
	{
		int elem;
		scanf("%d",&elem);
		nge_list[i] = elem;
	}
	nge_list[input_num] = -1;

	int nge_index = 0;
	while (1)
	{
		int find_index = nge_index +1;
		for (find_index;find_index < input_num ; find_index++)
		{
			if (nge_list[find_index] > nge_list[nge_index])
				break;
		}
		printf("%d ",nge_list[find_index]);
		if (nge_index++ > input_num-2) break;
	}
	return 0;	
}