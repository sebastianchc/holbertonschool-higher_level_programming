#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node in a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *tmp;

	if (!head)
	{
		return (0);
	}
	current = *head;
	tmp = current->next;
	new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (0);
	}
	new->n = number;
	if (new->n < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next)
	{
		if (new->n <= tmp->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
		tmp = tmp->next;
	}
	return(0);
}
