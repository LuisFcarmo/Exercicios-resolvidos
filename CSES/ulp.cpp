#include <iostream>
#include <string>
using namespace std;

int main () {
    bool valido = false;    
    int qtd;
    int i = 0;
    string palavra;    
    cin >> qtd;
    int v = 0;
    int tamanho;

    while (qtd--) {
        cin >> tamanho;
        cin >> palavra;
        for (int i = 0; i < palavra.length()-2; i++) {
            cout << palavra[i];
            if(v == 1) {
                if(
                    (palavra[i] == 'b' || palavra[i] == 'c' || palavra[i] == 'd') &&
                    (palavra[i+1] == 'b' || palavra[i+1] == 'c' || palavra[i+1] == 'd') 

                    ) {
                } else {
                    cout << '.';
                    v = 0;
                }
            }
            else if (palavra[i] == 'a' || palavra[i] == 'e') {
                v++;
            }
        }
        cout << "\n";
    }
    

    return 0;
}