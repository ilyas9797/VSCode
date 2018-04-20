#include <stdio.h>

typedef enum {false, true} bool;

int* InsertsSort(int mas[], int size, bool reverse)
{
    int x;
    int i, j;
    if (!reverse)
    {
        for (i = 0; i < size; i++)
        {
            x = mas[i];
            for (j = (i - 1); j >= 0 && mas[j] > x; j--)
            {
                mas[j + 1] = mas[j];
            }
            mas[j + 1] = x;
        }
    }
    else
    {
        for (i = 0; i < size; i++)
        {
            x = mas[i];
            for (j = (i - 1); j >= 0 && mas[j] < x; j--)
            {
                mas[j + 1] = mas[j];
            }
            mas[j + 1] = x;
        }
    }
    return mas;
}
