#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>
#include <ctype.h>

#define DllExport __declspec(dllexport)
#define len 256
#define num_len 8
#define filename "book.txt"

int n = 0;
struct Book
{
	char name[len];
	char author[len];
	char numberofpage[num_len];
	char rating[num_len];
};

DllExport int numberOfBooks()
{
	int cnt = 0;
	FILE* f = fopen(filename, "r");
	char k;
	if (f)
	{
		for (; !feof(f); cnt++)
			do
			{
				k = (char)fgetc(f);
			} while (k != '\n' && !feof(f));
			cnt--;
			n = cnt;
			fclose(f);
	}
	else
	{
		FILE *f = fopen(filename, "w");
		fclose(f);
	}
	return cnt;
}

void reading(char* field, char stop_symbol, FILE* f)
{
	int i = 0;
	char s;
	while ((s = (char)fgetc(f)) != stop_symbol)
	{
		field[i++] = s;
	}
	field[i++] = '\0';
}

void reading_from_file(struct Book* bk, FILE* f)
{
	reading(bk->name, ',', f);
	reading(bk->author, ',', f);
	reading(bk->numberofpage, ',', f);
	reading(bk->rating, '\n', f);
}

void writing_to_file(struct Book bk, FILE* f)
{
	fputs(bk.name, f);
	fputs(",", f);
	fputs(bk.author, f);
	fputs(",", f);
	fputs(bk.numberofpage, f);
	fputs(",", f);
	fputs(bk.rating, f);
	fputs("\n", f);
}


//field == 1 => сравниваем строки
//field == 2 => сравниваем числа
int cmp(char* a, char* b, int field)
{
	if (field == 1)
		return strcmp(a, b);
	else
		return atoi(a) - atoi(b);
}

void swap(struct Book *a, struct Book *b)
{
	struct Book t = *a;
	*a = *b;
	*b = t;
}

DllExport void sortBookByField(int field)
{
	FILE *f = fopen(filename, "r");
	if (f)
	{
		struct Book* bk = (struct Book*) malloc(sizeof(struct Book) * n);
		for (int i = 0; i < n; i++)
		{
			reading_from_file(&bk[i], f);
		}
		fclose(f);
		for (int i = 0; i < n - 1; i++)
		{
			for (int j = 0; j < n - 1; j++)
			{
				if (field == 1)
				{
					if (cmp(bk[j].name, bk[j + 1].name, 1) > 0)
						swap(&bk[j], &bk[j + 1]);
				}
				else if (field == 2)
				{
					if (cmp(bk[j].rating, bk[j + 1].rating, 2) < 0)
						swap(&bk[j], &bk[j + 1]);
				}
			}
		}
		f = fopen(filename, "w");
		for (int i = 0; i < n; i++)
			writing_to_file(bk[i], f);
		free(bk);
		fclose(f);
	}
}

DllExport int addBook(char* name, char* author, char* numberofpage, char* rating)
{
	struct Book bk;
	FILE* f = fopen(filename, "a");

	if (strlen(name) < len && strlen(author) < len && strlen(numberofpage) < num_len && strlen(rating) < num_len)
	{
		if (isdigit(numberofpage[0]) && isdigit(rating[0]))
		{
			strcpy(bk.name, name);
			strcpy(bk.author, author);
			strcpy(bk.numberofpage, numberofpage);
			strcpy(bk.rating, rating);
		}
	}

	writing_to_file(bk, f);

	++n;
	fclose(f);
	return n;
}

DllExport struct Book* output()
{
	FILE* f = fopen(filename, "r");
	if (f)
	{
		struct Book* bk = (struct Book*) malloc(sizeof(struct Book) * n);
		for (int i = 0; i < n; i++)
		{
			reading_from_file(&bk[i], f);
		}
		fclose(f);
		return bk;
	}
	else
	{
		return NULL;
	}
}

void deleteBook(struct Book *books, int i)
{
	for (; i < n; i++)
		books[i] = books[i + 1];
	--n;
}

DllExport int deleteBookByAuthor(char* author)
{
	FILE *f = fopen(filename, "r");
	if (f == NULL)
	{
		return -1;
	}
	struct Book* bk = (struct Book*) malloc(sizeof(struct Book) * n);
	for (int i = 0; i < n; i++)
	{
		reading_from_file(&bk[i], f);
	}
	fclose(f);
	for (int i = 0; i < n; i++)
		if (!strcmp(author, bk[i].author))
		{
			deleteBook(bk, i);
			i--;
		}
	f = fopen(filename, "w");
	for (int i = 0; i < n; i++)
		writing_to_file(bk[i], f);
	free(bk);
	fclose(f);

	return n;
}

//field == 1 => поиск по названию
//field == 2 => поиск по автору
DllExport int numberOfFindedBooks(int field, char* value)
{
	FILE* f = fopen(filename, "r");
	if (f)
	{
		int k = 0;
		struct Book bk;
		for (int i = 0; i < n; i++)
		{
			reading_from_file(&bk, f);
			switch (field)
			{
			case 1:
				if (cmp(bk.name, value, 1) == 0)
					k++;
				break;
			case 2:
				if (cmp(bk.author, value, 1) == 0)
					k++;
				break;
			default:
				break;
			}
		}
		fclose(f);
		return k;
	}
	else
	{
		return 0;
	}
}

//field == 1 => поиск по названию
//field == 2 => поиск по автору
DllExport struct Book* findByField(int field, char* value, int k)
{
	if (k == 0)
	{
		return NULL;
	}
	FILE* f = fopen(filename, "r");
	if (f)
	{
		struct Book bk;
		struct Book* p_bk = (struct Book*) malloc(sizeof(struct Book) * k);
		int j = 0;
		for (int i = 0; i < n; i++)
		{
			reading_from_file(&bk, f);
			switch (field)
			{
			case 1:
				if (cmp(bk.name, value, 1) == 0)
					p_bk[j++] = bk;
				break;
			case 2:
				if (cmp(bk.author, value, 1) == 0)
					p_bk[j++] = bk;
				break;
			default:
				break;
			}
		}
		fclose(f);
		return p_bk;
	}
	else
	{
		return NULL;
	}
}

DllExport int deleteBookByNumber(int k)
{
	FILE* f = fopen(filename, "r");
	if (f == NULL)
		return 0;
	if (k > n)
	{
		return n;
	}
	else
	{
		struct Book* bk = (struct Book*) malloc(sizeof(struct Book) * n);
		for (int i = 0; i < n; i++)
		{
			reading_from_file(&bk[i], f);
		}
		fclose(f);
		deleteBook(bk, k - 1);

		f = fopen(filename, "w");
		for (int i = 0; i < n; i++)
			writing_to_file(bk[i], f);
		free(bk);
		fclose(f);

		return n;
	}
}

DllExport void changeBook(int k, char* name, char* author, char* numberofpage, char* rating)
{
	int tmp = deleteBookByNumber(k);
	tmp = addBook(name, author, numberofpage, rating);
}
