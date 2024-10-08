#include "main.h"

int int_index(int *array, int size, int (*cmp)(int))
{
    int i;
    if (array && cmp)
    {
        if (size <=0)
        {
            return(-1);
        }
        for (i =0; i < size; i++)
        {
            if (cmp(array[i]))
            {
                return(i);
            }
        }
    }
    return (-i);
}