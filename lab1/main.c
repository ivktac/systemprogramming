#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void parse(char *str, const char *pattern)
{
  char *copy = strdup(str);
  char *ptr = str;

  bool flag = true;
  while (*ptr && *pattern)
  {
    if (*pattern == '{')
    {
      char ch = *(pattern + 1);
      int num = atoi(pattern + 3);

      int count = 0;
      while (*ptr == ch)
      {
        count++;
        ptr++;
      }

      if (count != num)
      {
        flag = false;
        break;
      }

      memmove(ptr - num, ptr, strlen(str) - (ptr - str - 1) + 1);

      ptr -= num;

      pattern = strchr(pattern, '}');
      if (pattern == NULL)
      {
        flag = false;
        printf("ERROR: Missing '}' in pattern\n");
        break;
      }
      pattern++;

      continue;
    }

    if (*ptr != *pattern)
    {
      flag = false;
      break;
    }

    ptr++;
    pattern++;
  }

  if (!flag)
  {
    strcpy(str, copy);
    free(copy);
  }
}

int main()
{
  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("output.txt", "w");

  char pattern[100];

  printf("Enter pattern: ");
  scanf("%s", pattern);

  if (in == NULL || out == NULL)
  {
    printf("Error opening file\n");
    return 1;
  }

  fseek(in, 0, SEEK_END);
  long size = ftell(in);
  rewind(in);

  char *strs = (char *)malloc(size * sizeof(char));
  if (strs == NULL)
  {
    printf("Error allocating memory\n");
    return 1;
  }

  fread(strs, sizeof(char), size, in);

  if (strs[size - 1] == '\n')
    strs[size - 1] = '\0';

  char *str = strtok(strs, " ");

  while (str != NULL)
  {
    char *copy = strdup(str);
    parse(copy, pattern);
    fprintf(out, "%s ", copy);
    str = strtok(NULL, " ");
  }

  fclose(in);
  fclose(out);

  return 0;
}