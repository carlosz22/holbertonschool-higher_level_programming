#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - prints all elements of a listint_t list
 * @head: double pointer to head of list
 * @number: Number to insert in the new node
 * Return: Pointer to the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (current == NULL || number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current != NULL)
	{
		if (number > current->n)
		{
			previous = current;
			current = current->next;
		}
		else
			break;
	}

	previous->next = new;
	new->next = current;
	return (new);
}
