#include "lists.h"

listint_t *create_node(int n);

/**
 * insert_node - setgestgatgr
 * @head: aergaerg
 * @number: asrgaegser
 *
 * Return: 0
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur_node = NULL, *new_node = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		new_node = create_node(number);
		*head = new_node;
		return (new_node);
	}
	cur_node = *head;
	while (cur_node)
	{
		if (cur_node->n >= number)
		{
			new_node = create_node(number);
			new_node->next = cur_node;
			*head = new_node;
			return (new_node);
		}
		else if (cur_node->n <= number)
		{
			if (!cur_node->next || cur_node->next->n >= number)
			{
				new_node = create_node(number);
				new_node->next = cur_node->next;
				cur_node->next = new_node;
				return (cur_node->next);
			}
		}
		cur_node = cur_node->next;
	}
	return (NULL);
}


/**
 * create_node - regtegertge
 * @n: greagrfae
 *
 * Return: 0
 */
listint_t *create_node(int n)
{
	listint_t *ret = NULL;

	ret = malloc(sizeof(listint_t));
	if (!ret)
		return (NULL);
	ret->next = NULL;
	ret->n = n;
	return (ret);
}
