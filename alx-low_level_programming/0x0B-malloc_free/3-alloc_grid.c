#include "main.h"
#include <stdio.h>

int **alloc_grid(int widith, int height)
{
    int **gridout;
    int i,j;
    if (widith <1 || height < 1)
    {
        return NULL;
    }

    gridout = malloc(height * sizeof(int *));
    if (gridout == NULL)
    {
        free(gridout);

        return NULL;
    }
    for (i =0; i < height; i++)
    {
        gridout[i] = malloc(widith * sizeof(int));
        if (gridout[i] == NULL)
        {
            for (i--; i >=0; i--)
            {
                free(gridout[i]);
            }
            free(gridout);
            return NULL;
        }
    }
    for (i =0; i < height; i++)
    {
        for (j=0; j < widith; j++)
        {
            gridout[i][j] =0;
        }
    }
    return (gridout);

}