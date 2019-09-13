#include "lists.h"

/**
 * add_dnodeint_end - add node at the end
 * @head: Head pointer
 * @n: Value to insert in the new node
 *
 * Return: New node or NULL if fails.
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *next_node = head;
	dlistint_t *current_node = head;

	while (current_node != NULL)
	{
		next_node = current_node->next;
		free(current_node);
		current_node = next_node;
	}
}
