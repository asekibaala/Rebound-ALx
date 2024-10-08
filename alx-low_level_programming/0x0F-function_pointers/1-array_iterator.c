#include "main.h"

void array_iterator(int *array, size_t size, void (*action)(int))
{
    unsigned int i;
    if(array && action)
    {
        for (i=0; i < size; i++)
        {
            action(array[i]);
        }
    }
}