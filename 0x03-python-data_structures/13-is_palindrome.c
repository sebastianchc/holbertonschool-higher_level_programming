#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome or not
 * @head: pointer to head of list
 *
 * Return: 1 if the list i palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *count = *head, *check;
	unsigned int nodes = 0, i = 0, plndrm = 0;

	while (count)
	{
		count = (*count).next;
		nodes++;
	}
	while (i <= nodes / 2)
	{
		check = *head;
		while ((*check).next)
		{
			check = (*check).next;
		}
		if ((*check).n == (**head).n)
		{
			plndrm = 1;
			(*check).next = NULL;
		}
		else
		{
			return (0);
		}
		*head = (**head).next;
	}
	return (plndrm);
}
