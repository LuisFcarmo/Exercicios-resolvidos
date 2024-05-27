#include <iostream>

using namespace std;

int main () {
    int qtd;
    int numero, numero2, numero3;
    cin >> qtd;
    while(qtd--) {
        cin >> numero >> numero2 >> numero3;
        if (numero3 == numero) {
            cout << numero2;
        }
        else if(numero2 == numero3) {
            cout << numero;
        }
        else {
            cout << numero3;
        }
        cout << endl;
    }
  
    return 0;
}