#include <stdio.h>
#include <stdlib.h>

const int STR_LENGTH = 30;

int string_comp(char *a, char *b)
{
    for (int i = 0; i < STR_LENGTH; i++)
    {
        if (a[i] != b[i])
        {
            if (a[i] < b[i])
            {
                return -1;
            }
            else
            {
                return 1;
            }
        }
    }
    return 0;
}

char *readString()
{
    char *answer = (char *)malloc(STR_LENGTH * sizeof(char));
    char ch = getchar();
    for (int i = 0; i < STR_LENGTH; i++)
    {
        if (ch == '\n')
        answer[i] = ch;
    }
    return answer;
}

struct Vertex
{
    char *name;
    char *num;
    struct Vertex *l; //left
    struct Vertex *r; //right
};

struct Vertex root;
int size = 0;

void inic(char *name, char *num)
{
    size++;
    root.name = name;
    root.num = num;
    root.l = NULL;
    root.r = NULL;
}

void add_(struct Vertex *f, char *name, char *num)
{
    if (size == 0)
    {
        printf("ADDING ROOT\n");
        inic(name, num);
        return;
    }
    int cmp = string_comp(name, f->name);
    if (cmp == 0)
    {
        f->num = num;
        return;
    }
    if (cmp == 1)
    {
        if (f->r != NULL)
            add_(f->r, name, num);
        else
        {
            size++;
            struct Vertex *new_node = (struct Node *)malloc(sizeof(struct Vertex));
            new_node->l = NULL;
            new_node->r = NULL;
            new_node->name = name;
            new_node->num = num;
            f->r = new_node;
        }
    }
    else
    {
        if (f->l != NULL)
        {
            add_(f->l, name, num);
        }
        else
        {
            size++;
            struct Vertex *new_node = (struct Node *)malloc(sizeof(struct Vertex));
            new_node->l = NULL;
            new_node->r = NULL;
            new_node->name = name;
            new_node->num = num;
            f->l = new_node;
        }
    }
}

void add(char *name, char *num)
{
    add_(&root, name, num);
}

void del_(struct Vertex *parent, struct Vertex *f, char *name)
{
    int cmp = string_comp(name, f->name);
    if (cmp == 1)
    {
        if (f->r == NULL)
        {
            printf("NO ELEMET\n");
            return;
        }
        del_(f, f->r, name);
        return;
    }
    if (cmp == -1)
    {
        if (f->l == NULL)
        {
            printf("NO ELEMENT\n");
            return;
        }
        del_(f, f->l, name);
        return;
    }
    if (f->l == NULL && f->r == NULL)
    {
        if (parent->l == f)
        {
            parent->l = NULL;
        }
        else
        {
            parent->r = NULL;
        }
        free(f);
        size--;
        return;
    }

    if (f->l == NULL)
    {
        struct Vertex *r = f->r;
        // f->l = r->l;
        // f->r = r->r;
        parent->l = r->l;
        f->name = r->name;
        f->num = r->num;
        free(r);
        size--;
        return;
    }
    if (f->r == NULL)
    {
        struct Vertex *l = f->l;
        f->l = l->l;
        f->r = l->r;
        f->name = l->name;
        f->num = l->num;
        free(l);
        size--;
        return;
    }

    struct Vertex *tmp = f->l;
    struct Vertex *parent_tmp;
    while (tmp->r != NULL)
    {
        parent = tmp;
        tmp = tmp->r;
    }

    if (tmp == f->l)
    {
        tmp->r = f->r;
        if (parent->r == f)
        {
            parent->r = tmp;
        }
        else
        {
            parent->l = tmp;
        }
        free(f);
        size--;
        return;
    }
    parent->r = tmp->l;
    f->num = tmp->num;
    f->name = tmp->name;
    free(tmp);
    size--;
}

void del(char *name)
{
    del_(&root, &root, name);
}

void dfs_(struct Vertex *f)
{
    if (f->l != NULL)
    {
        dfs_(f->l);
    }
    printf("name: ");
    print(f->name, 0);
    printf(" number: ");
    print(f->num, 1);
    printf("\n");
    if (f->r != NULL)
    {
        dfs_(f->r);
    }
}

void dfs()
{
    if (size == 0)
    {
        printf("NO ELEMENTS\n");
        return;
    }
    dfs_(&root);
}

void print(char *a, int type)
{
    for (int i = 0; i < STR_LENGTH; i++)
    {
        if (a[i] == ' ' && type)
            break;
        printf("%c", a[i]);
    }
}

void get_(struct Vertex *f, char *name)
{
    int cmp = string_comp(name, f->name);
    if (cmp == 1)
    {
        if (f->r == NULL)
        {
            printf("NO ELEMENT\n");
            return;
        }
        get_(f->r, name);
        return;
    }
    if (cmp == -1)
    {
        if (f->l == NULL)
        {
            printf("NO ELEMENT\n");
            return;
        }
        get_(f->l, name);
        return;
    }
    printf("NUMBER IS: ");
    print(f->num, 1);
    printf("\n");
}

void get(char *name)
{
    if (size == 0)
    {
        printf("NO ELEMENTS\n");
        return;
    }
    get_(&root, name);
}

int eq(char *a, char *b)
{
    for (int i = 0; i < 3; i++)
    {
        if (a[i] != b[i])
            return 0;
    }
    return 1;
}

int main()
{
    char *in = readString();
    while (!eq(in, "end"))
    {
        if (eq(in, "add"))
        {
            printf("Name: ");
            char *name = readString();
            printf("Number: ");
            char *number = readString();
            add(name, number);
            in = readString();
            continue;
        }
        if (eq(in, "del"))
        {
            printf("Name: ");
            char *name = readString();
            del(name);
            in = readString();
            continue;
        }
        if (eq(in, "dfs"))
        {
            dfs();
            in = readString();
            continue;
        }
        if (eq(in, "get"))
        {
            printf("Name: ");
            char *name = readString();
            get(name);
            in = readString();
            continue;
        }
        printf("Try again\n");
        in = readString();
    }
    return 0;
}
