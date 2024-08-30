#include "stdio.h"
#include "stdlib.h"

int main (int argc, char *argv[]) {
    char comand[500];
    snprintf(comand, sizeof(comand), 
             "git status && git add . && git commit -m \"%s\" && git push", 
             argv[1]);

    int result = system(comand);

    if (result == -1) {
        perror("system");
        return 1;
    }
    return 0;
}