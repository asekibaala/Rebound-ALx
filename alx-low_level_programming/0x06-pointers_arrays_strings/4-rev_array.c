#include "main.h"
void reverse_array(int *a, int n)
{
    int i, j, temp;
    for(i =0; i < n - 1; i++)
    {
        for (j = 1 + 1; j > 0; j--)
        {
            temp = *(a + j);
            *(a + j) = *(a + (j - 1));
            *(a + (j - 1)) = temp;
        }
    }
}