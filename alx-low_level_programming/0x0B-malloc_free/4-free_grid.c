#include "main.h"
#include <stdio.h>

void free_grid(int **grid, int height)
{
    if (grid != NULL && height !=0)
    {
        for (; height >=0; height--)
        {
            free(grid[height]);
        }
        free(grid);
    }
}