#include <stdio.h>
#include <string.h>

int prep(char *a)
{
    //не изменится, если длинна строки > BUFSIZE символов
    int indicator = 1;
    for (int i = 0; i < BUFSIZ; i++)
    {
        if (*(a + i) == '\n' || *(a + i) == EOF)
        {
            *(a + i) = '\0';
            indicator = 0;
            break;
        }
    }
    if (indicator)
    {
        return 1;
    }
    return 0;
}

int main()
{
    char a[BUFSIZ], b[BUFSIZ];
    //puts("Enter first file path");
    //gets(a);
    FILE *pa = fopen("1.txt", "r");
    if (!pa)
    {
        //интерпретирует значение глобальной переменной ERRNO в строку и выводит эту строку на стандартный поток вывода
        perror("Error -- file '1.txt' not found");
        return 1;
    }
    //puts("Enter second file path");
    //gets(b);
    FILE *pb = fopen("2.txt", "r");
    if (!pb)
    {
        perror("Error -- file '2.txt' not found");
        return 2;
    }
    int line = 1;
    while (!(feof(pa) || feof(pb)))
    {
        //считывает символы из потока и сохраняет их в виде строки в параметр string до тех пор пока не наступит конец строки или пока не будет достигнут конец файла
        //проверка на случай пустой строки
        if (!fgets(a, sizeof(a), pa))
            *a = '\n';
        if (!fgets(b, sizeof(b), pb))
            *b = '\n';
        if (prep(a))
        {
            printf("Error -- string %d in file '1.txt' are too long (should be < %d)\n", line, BUFSIZ);
            break;
        }        
        if (prep(b))
        {
            printf("Error -- string %d in file '2.txt' are too long (should be < %d)\n", line, BUFSIZ);
            break;
        }
        if (strcmp(a, b))
        {
            printf("\nline %d:\n", line);
            printf("file1: --> %s\n", a);
            printf("file2: --> %s\n", b);
        }
        ++line;
    }
    fclose(pa);
    fclose(pb);
    return 0;
}
