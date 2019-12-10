#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Function in C that checks if a lisint_t list has a cycle in it.
 * @list: head of listint_t list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
	{
		return (0);
	}
	while (list)
	{
		temp = list;
		list = (*list).next;
		if (temp <= list)
		{
			return (1);
		}
	}
	return (0);
}
