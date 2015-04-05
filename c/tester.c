#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "shittydb.h"

int main(int argc, char ** argv) {
    char key[] = "test";
    char val[] = "woah i sure hope this works";

    if (shittydb_set(key, val)) return EXIT_FAILURE;

    char * result = NULL;

    if (shittydb_get(&result, key)) return EXIT_FAILURE;

    if (strcmp(val, result)) {
        free(result);
        return EXIT_FAILURE;
    }

    free(result);
    return EXIT_SUCCESS;
}
