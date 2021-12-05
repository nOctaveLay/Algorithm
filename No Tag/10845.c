#include <stdio.h>
#include <string.h>
#define MAX 10001

typedef struct __queue{
	int first;
	int last;
	int list[MAX];
}Queue;

void init_queue(Queue *q)
{
	q->first = 0;
	q->last = 0;
}
int isEmpty(Queue *q)
{return (q->last - q->first) == 0 ? 1 : 0;}

void enqueue(Queue *q, int data)
{
	q->list[q->last] = data;
	q->last += 1;
}

void dequeue(Queue *q)
{
	if (!isEmpty(q)) q->first += 1;
}


int first(Queue *q)
{return isEmpty(q) ? -1 : q->list[q->first];}

int last(Queue *q)
{return isEmpty(q) ? -1 :q->list[q->last-1];}

int size(Queue *q)
{return (q->last - q->first);}



int main()
{
	int input_num;
	scanf("%d",&input_num);
	Queue q;
	init_queue(&q);
	while (input_num--)
	{
		char command[6];
		scanf("%s",&command);
		if (!strcmp(command,"push"))
		{
			int element;
			scanf("%d",&element);
			enqueue(&q,element);
		}
		else if (!strcmp(command,"pop")) 
		{
			printf("%d\n",first(&q));
			dequeue(&q);
		}

		else if (!strcmp(command,"front")) printf("%d\n",first(&q));
		else if (!strcmp(command,"back")) printf("%d\n",last(&q));
		else if (!strcmp(command,"size")) printf("%d\n",size(&q));
		else if (!strcmp(command,"empty")) printf("%d\n",isEmpty(&q));
	}
}