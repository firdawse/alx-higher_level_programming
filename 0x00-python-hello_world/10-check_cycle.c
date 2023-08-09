#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list concerned
 *
 * Return: 1 if list is a cyclye 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	if (!list)
		return (0);

	while (ptr1 && ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}

	return (0);
}

