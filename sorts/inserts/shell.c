#include <stdio.h>

#include <stdio.h>

typedef enum {false, true} bool;

struct Inc{
    int s;
    int *inc_seq;
};

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

struct Inc increment(int inc[], int size)
{
    int s = 0;
    int p1, p2, p3 = 1;
    do
    {
        if (s % 2 == 0){
            inc[s++] = 9 * p1 - 9 * p2 + 1;
            p2 *= 2;
            p3 *= 2;
        }
        else
        {
            inc[s++] = 8 * p1 - 6 * p3 + 1;
        }
        p1 *= 2;
    } while(inc[s] * 3 < size);
    struct Inc inc_struct;
    inc_struct.s = s - 1;
    inc_struct.inc_seq = inc;
    return inc_struct;
}

int* ShellSort(int mas[], int size, bool reverse)
{
    int inc_seq[40];
    int inc, x, i, j, s;
    struct Inc inc_struct = increment(inc_seq, size);
    if (!reverse)
    {
        for (s = inc_struct.s; s >= 0; s--)
        {
            inc = inc_struct.inc_seq[s];
            for (i = inc; i < size; i += inc)
            {
                x = mas[i - inc];
                for (j = i - inc; j >= 0 && mas[j] > x; j -= inc)
                {
                    mas[j + inc] = mas[j];
                }
                mas[j + inc] = x;
            }
        }
    }
    else
    {
        for (s = inc_struct.s; s >= 0; s--)
        {
            inc = inc_struct.inc_seq[s];
            for (i = inc; i < size; i += inc)
            {
                x = mas[i - inc];
                for (j = i - inc; j >= 0 && mas[j] < x; j -= inc)
                {
                    mas[j + inc] = mas[j];
                }
                mas[j + inc] = x;
            }
        }
    }
    return mas;
}