#include <stdlib.h>
#include <stdio.h>

#define GIVEUP(file) { fclose(file); return 1; }

int shittydb_get(char ** val, const char * key) {
    FILE * file = fopen(key, "r");
    if (!file) return 1;

    if (fseek(file, 0, SEEK_END)) GIVEUP(file);

    long off = ftell(file);
    if (off < 0) GIVEUP(file);

    if (fseek(file, 0, SEEK_SET)) GIVEUP(file);

    char * response = malloc(off + 1);
    if (!response) GIVEUP(file);

    if (fread(response, sizeof(*response), off, file) != off) GIVEUP(file);

    response[off] = '\0';

    fclose(file);
    *val = response;
    return 0;
}

int shittydb_set(const char * key, const char * val) {
    FILE * file = fopen(key, "w");
    if (!file) GIVEUP(file);

    fprintf(file, "%s", val);

    fclose(file);
    return 0;
}
