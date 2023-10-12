#include "lists.h"

/**
 *  * print_dlistint - Prints all the elements of a dlistint_t list
 *   * @h: A pointer to the head of the list
 *    * Return: The number of nodes in the list
 *     */
size_t print_dlistint(const dlistint_t *h)
{
	int count;
	count = 0;

	if (h == NULL)
		return (count);
	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
