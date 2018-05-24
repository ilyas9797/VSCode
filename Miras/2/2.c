#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

typedef struct Node
{
	int info;
	struct Node *next;
	struct Node *prev;
} Node;

int Add(Node **p, int num, int pos)
{
	Node *tmp = (Node *)malloc(sizeof(Node));
	if (tmp == NULL)
	{
		perror("Error -- add error");
		return 1;
	}
	tmp->info = num;
	//если список пустой
	if (*p == NULL)
	{
		tmp->next = NULL;
		tmp->prev = NULL;
		*p = tmp;
		puts("List succesful created");
	}
	//если вписок непустой
	else
	{
		//запись в начало списка
		if (pos == 1)
		{
			tmp->next = *p;
			tmp->prev = NULL;
			(*p)->prev = tmp;
			*p = tmp;
			puts("Item succesful added to begin");
		}
		//запись в конец списка
		else
		{
			Node *last_node = *p;
			while (last_node->next != NULL)
			{
				last_node = last_node->next;
			}
			tmp->next = NULL;
			tmp->prev = last_node;
			last_node->next = tmp;
			puts("Item succesful added to end");
		}
	}
	printf("\n");
	
	return 0;
}

int Del(Node **p, int num)
{
	if (*p == NULL)
	{
		puts("Error -- list is empty");
		return 1;
	}
	Node *tmp = *p;
	int indicator = 1;
	while (tmp != NULL)
	{
		if (tmp->info == num)
		{
			if (tmp->prev != NULL)
				tmp->prev->next = tmp->next;
			if (tmp->next != NULL)
				tmp->next->prev = tmp->prev;
			if (tmp == *p)
				*p = tmp->next;
			free(tmp);
			puts("Item succesful deleted");
			indicator = 0;
			break;
		}
		tmp = tmp->next;
	}
	if (indicator)
		puts("Item was not found");
	return 0;
}

int Show(Node *p)
{
	if (p == NULL)
	{
		puts("Error -- list is empty");
		return 1;
	}

	Node *tmp = p;
	printf("\n");
	puts("list begin");
	printf("   ^v\n   ||\n   ||\n   ^v\n");
	while (tmp != NULL)
	{
		printf("  Item: %d\n", tmp->info);
		printf("   ^v\n   ||\n   ||\n   ^v\n");
		tmp = tmp->next;
	}
	puts("list end");

	return 0;
}

int main()
{
	Node *list = NULL;
	int num = 0;
	int q = 0;		
	printf("\n   Commands:\n1) Add item in begin;\n2) Add item in end;\n3) Delete item;\n4) Show list;\n5) Exit program.\n\nEnter command (only number!):\n>>>");
	scanf("%d", &q);
	while (q != 5)
	{
		if (q == 1 || q == 2)
		{
			printf("\nWrite added item (only number!):\n>>>");
			scanf("%d", &num);
			Add(&list, num, q);
		}
		else if (q == 3)
		{
			printf("\nWrite deleted item (only number!):\n>>>");
			scanf("%d", &num);
			Del(&list, num);			
		}
		else if (q == 4)
		{
			Show(list);
		}
		else if (q != 5)
		{
			printf("Error -- command was not found\n");
			q = 0;
		}
		printf("\nEnter command (only number!):\n>>>");
		scanf("%d", &q);
	}
	system("pause");
}
