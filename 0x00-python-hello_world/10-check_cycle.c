#include "lists.h"

/**
 * check_cycle - checks the continuation of a linked list cycle
 * @list: linked list.
 *
 * Return: 1 if a cycle exits, 0 if co cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
