#include "lists.h"

/**
 * add_dnodeint - add node at the beginning
 * @head: Head pointer
 * @n: Value to insert in the new node
 *
 * Return: New node or NULL if fails.
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	new->prev = NULL;
	if (*head != NULL)
		(*head)->prev = new;
	*head = new;

	return (new);
}
