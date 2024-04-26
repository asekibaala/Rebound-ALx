#include "sort.h"

void bubble_sort(int *array, size_t size)
{
    size_t i=0, j=0;
    int aux =0;

    if(array ==NULL || size ==0)
    {
        return;
    }
    for (; i<size; i++)
    {
        for(j=0; j<size - i -1; j++)
        {
            if (array[j] > array[j + 1])
            {
                aux = array[j + 1];
                array[j + 1] = array[j];
                array[j]=aux;
                print_array(array,size);
            }
        }
    }

}