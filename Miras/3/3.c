#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LENGTH 256

struct tree
{
    char name[LENGTH];
    char number[LENGTH];
    struct tree *left;
    struct tree *right;
};

struct tree *stree(struct tree *root, struct tree *r, char *name, char *number)
{
    if (strlen(name) >= LENGTH && strlen(number) >= LENGTH)
    {
        printf("Error -- strings are too long\n");
        return NULL;
    }
    if (!r)
    {
        r = (struct tree *)malloc(sizeof(struct tree));
        if (!r)
        {
            printf("Error -- malloc error\n");
            return NULL;
        }
        r->left = NULL;
        r->right = NULL;
        strcpy(r->name, name);
        strcpy(r->number, number);
        if (!root)
            return r; /* первый вход */
        if (strcmp(name, root->name) == -1)
            root->left = r;
        else
            root->right = r;
        return r;
    }
    if (strcmp(name, r->name) == -1)
        stree(r, r->left, name, number);
    else
        stree(r, r->right, name, number);
    return root;
}

void inorder(struct tree *root)
{
    if (!root)
        return;
    inorder(root->left);
    printf("\n");
    puts(root->name);
    puts(root->number);
    printf("\n");
    inorder(root->right);
}

struct tree *search_tree(struct tree *root, char *name)
{
    if (!root)
        return root; /* пустое дерево */
    int cmp = strcmp(name, root->name);
    while (!cmp)
    {
        if (cmp == -1)
            root = root->left;
        else
            root = root->right;
        if (root == NULL)
            break;
    }
    return root;
}

struct tree *dtree(struct tree *root, char *name)
{
    struct tree *p, *p2;

    if (!root)
        return root; /* вершина не найдена */

    int cmp = strcmp(name, root->name);
    if (!cmp)
    { /* удаление корня */
        /* это означает пустое дерево */
        if (root->left == root->right)
        {
            free(root);
            return NULL;
        }
        /* или если одно из поддеревьев пустое */
        else if (root->left == NULL)
        {
            p = root->right;
            free(root);
            return p;
        }
        else if (root->right == NULL)
        {
            p = root->left;
            free(root);
            return p;
        }
        /* или есть оба поддерева */
        else
        {
            p2 = root->right;
            p = root->right;
            while (p->left)
                p = p->left;
            p->left = root->left;
            free(root);
            return p2;
        }
    }
    if (cmp == 1)
        root->right = dtree(root->right, name);
    else
        root->left = dtree(root->left, name);
    return root;
}

int main()
{
    struct tree *tree = NULL;
    int q = 0;
    char name[LENGTH];
    char number[LENGTH];

    printf("\n   Commands:\n1) Add item;\n2) Delete item;\n3) Show list;\n4)Search;\n5) Exit program.\n\nEnter command (len < %d):\n>>>", LENGTH);
    scanf("%d", &q);
    while (q != 5)
    {
        getchar();
        if (q == 1)
        {
            printf("\nWrite added item (len < %d):\n(name)>>>", LENGTH);
            gets(name);
            printf("(number)>>>");
            getchar();
            gets(number);
            tree = stree(tree, tree, name, number);
        }
        else if (q == 2)
        {
            printf("\nWrite deleted item (len < %d):\n(name)>>>");
            gets(name);
            tree = dtree(tree, name);
        }
        else if (q == 3)
        {
            inorder(tree);
        }
        else if (q == 4)
        {
            printf("\nWrite deleted item (len < %d):\n(name)>>>");
            gets(name);
            struct tree *tmp = search_tree(tree, name);
            if (tmp)
            {
                printf("\n");
                puts(tmp->name);
                puts(tmp->number);
                printf("\n");
            }
            else
            {
                puts("Item was not found\n");

            }
        }
        else if (q != 5)
        {
            printf("Error -- command was not found\n");
            q = 0;
        }
        printf("\nEnter command (only number!):\n>>>");
        scanf("%d", &q);
    }
    system("pause");
    return 0;
}
