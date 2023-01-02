#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * Description: For optimal performance, this function
 * assumes that a circular linked list would circle back to
 * the head of the list (this is the common linked list implementation
 * @list: a node in a linked list
 * Return: 1 if a cycle was found, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (!(list && list->next))
		return (0);

	tortoise = list->next;
	hare = list->next->next;
	if (tortoise == list || hare == list || tortoise == hare)
		return (1);

	while (hare && hare->next)
	{
		if (tortoise == hare || tortoise == hare->next)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}

