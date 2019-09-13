#include "lists.h"

/**
 * print_dlistint - print the linked list
 * @h: Head pointer
 *
 * Return: Number of nodes.
 */

size_t print_dlistint(const dlistint_t *h)
{
	int i = 0;
	const dlistint_t *tmp;

	tmp = h;

	while (tmp != NULL)
	{
		printf("%d\n", tmp->n);
		tmp = tmp->next;
		i++;
	}

	return (i);
}
