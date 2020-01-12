#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it.
 * @list: Pointer to list.
 *
 * Return: 0 there is no cycle, 1 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *tmp;

	current = list;
	tmp = list;
	while (tmp)
	{
		current = current->next;
		if (!current)
		{
			return (0);
		}
		tmp = tmp->next;
		tmp = tmp->next;
		if (tmp == current)
		{
			return (1);
		}
	}
	return (0);
}
