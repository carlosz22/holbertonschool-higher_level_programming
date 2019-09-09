#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - check for cycle in the linked list
 * @list: pointer to head of list
 * Return: 1 - has cycle or 0 - has no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		if (!(fast && fast->next && fast->next->next))
			return (0);
		fast = fast->next;
		fast = fast->next;
		slow = slow->next;
		if (fast == slow)
			break;
	}
	return (1);
}
