#include <stdio.h>
#include <stdlib.h>
#include "13-main.c"

/* Define the structure for a singly linked list node */
struct listint_s {
    int n;
    struct listint_s *next;
};

typedef struct listint_s listint_t;

/* Function to check if a singly linked list is a palindrome */
int is_palindrome(listint_t **head)
{
    if (*head == NULL)
        return (1);

    /* Slow and fast pointers to find the middle of the linked list */
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    /* Move fast pointer two steps and slow pointer one step */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        /* Reverse the first half of the linked list */
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    /* If the number of elements is odd, move slow pointer one step forward */
    if (fast != NULL)
        slow = slow->next;

    /* Compare the reversed first half with the second half */
    while (slow != NULL)
    {
        if (slow->n != prev->n)
            return (0);

        slow = slow->next;
        prev = prev->next;
    }

    return (1);
}