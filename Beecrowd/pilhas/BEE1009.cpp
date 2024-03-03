#include <stack>
#include <iostream>
#include <string.h>
int main () {
    using namespace std;
    char mina[1001] = "";
    stack <int>  stack_abre;
    stack <int> stack_fecha;
    int casos_teste = 0;
    int qtd = 0;
    scanf("%d", &casos_teste);    
    while (casos_teste--) {
        scanf("%s%*c", mina);

        for (int i = 0; i < strlen(mina); i++) {
            if (mina[i] == '<') {
                stack_abre.push(1);
            }
            if (mina[i] == '>') {
                stack_fecha.push(2);
            }
        }

        while (stack_abre.size() != 0 && stack_fecha.size() != 0) {
            stack_abre.pop();
            stack_fecha.pop();
            qtd++;
        }

        printf("%d", qtd);
        qtd = 0;
    }
    return 0;
}