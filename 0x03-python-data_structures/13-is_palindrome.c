#include "lists.h"
/**
 * is_palindrome - check if a linked list is a palindrome.
 * @head: Head pointer
 *
 * Return: 1 if is palidrome or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	int nodes = 0;
	int i = 0;
	int j = 0;
	int list[1000];

	if (*head == NULL)
		return (1);

	while (*head != NULL)
	{
		list[nodes] = (*head)->n;
		*head = (*head)->next;
		nodes++;
	}

	i = nodes - 1;

	while (i >= 0)
	{
		if (list[i] != list[j])
			return (0);
		i--;
		j++;
	}
	return (1);
}
