#include "main.h"
#include <stdlib.h>

/**
 * _strdup - returns a pointer to a newly allocated space in memory
 * @str: string
 * Return: pointer
 */
void *malloc_checked(unsigned int b)
{
    char *p;
    p = malloc(b);
    if (p == NULL)
    {
        exit(98);

    }
    return (p);
}