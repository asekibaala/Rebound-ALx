#include "main.h"
#include <stdio.h>

int *array_range(int min, int max)
{
    int *ptr_ar;
    int i;
    if (min > max)
    {
        return NULL;
    }
    ptr_ar = malloc(sizeof(*ptr_ar) * ((max - min) + 1));
    if (ptr_ar == NULL)
    {
        return NULL;
    }
    i =0;
    while (min <= max)
    {
        ptr_ar[i] = min;
        i++; min++;
    }
    return ptr_ar;  
    
}