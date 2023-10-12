#include "lists.h"

/**
 *  * dlistint_len - Returns the number of elements in a dlistint_t list
 *   * @h: A pointer to the head of the list
 *    * Return: The number of nodes in the list
 *     */
size_t dlistint_len(const dlistint_t *h)
{
	int count;
	count = 0;

	if (h == NULL)
		return (count);
	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}
