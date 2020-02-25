#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it.
 * @list: Pointer to list.
 *
 * Return: 0 there is no cycle, 1 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
